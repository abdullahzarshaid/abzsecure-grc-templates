"""Read-only structural checks, not native Excel calculation verification."""
import hashlib
import json
from pathlib import Path
import zipfile
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parents[1]
expected = {
    "assessment-scope.xlsx", "evidence-register.xlsx", "policy-register.xlsx",
    "remediation-tracker.xlsx", "risk-register.xlsx", "vendor-review.xlsx",
}
actual = {path.name for path in (root / "templates").glob("*.xlsx")}
assert actual == expected, "Unexpected or missing workbooks"
hashes = json.loads((root / "checksums.json").read_text(encoding="utf-8"))
assert set(hashes) == expected, "Checksum inventory differs"
ns = {"s": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
for name in sorted(expected):
    path = root / "templates" / name
    assert hashlib.sha256(path.read_bytes()).hexdigest() == hashes[name], name
    with zipfile.ZipFile(path) as archive:
        assert archive.testzip() is None, name
        entries = archive.namelist()
        assert not any("vba" in entry.lower() or "externallinks" in entry.lower() for entry in entries), name
        assert "[Content_Types].xml" in entries and "xl/workbook.xml" in entries, name
        sheets = [entry for entry in entries if entry.startswith("xl/worksheets/sheet") and entry.endswith(".xml")]
        assert len(sheets) == 1, name
        sheet = ET.fromstring(archive.read(sheets[0]))
        assert sheet.find("s:sheetViews/s:sheetView/s:pane", ns) is not None, name
        assert sheet.find("s:dataValidations", ns) is not None, name
        tables = [entry for entry in entries if entry.startswith("xl/tables/table") and entry.endswith(".xml")]
        assert len(tables) == 1, name
        table = ET.fromstring(archive.read(tables[0]))
        # Row 10 is the table header; rows 11 through 110 are 100 blank inputs.
        assert table.attrib["ref"].startswith("A10:") and table.attrib["ref"].endswith("110"), (name, table.attrib["ref"])
print(json.dumps({"status": "pass", "workbooks": len(expected), "checks": "hashes, ZIP/XML, prepared ranges, panes, validation, no macros or external links", "native_excel_calculation": "not tested"}))
