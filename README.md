# ABZSECURE GRC starter templates

[![Template integrity](https://github.com/abdullahzarshaid/abzsecure-grc-templates/actions/workflows/templates.yml/badge.svg)](https://github.com/abdullahzarshaid/abzsecure-grc-templates/actions/workflows/templates.yml)

Six original blank Excel trackers for small teams organizing security work in spreadsheets. Each file has 100 prepared rows, status dropdowns, filters and a frozen header. No macros or customer records are included.

## Downloads

- [Risk register](templates/risk-register.xlsx): risk owners, treatment and organization-defined likelihood × impact scoring.
- [Evidence register](templates/evidence-register.xlsx): evidence requests, references, reviewers and expiry dates.
- [Remediation tracker](templates/remediation-tracker.xlsx): gaps, owners, deadlines and completion evidence.
- [Vendor review](templates/vendor-review.xlsx): due diligence and follow-up.
- [Policy register](templates/policy-register.xlsx): versions, approvers and review dates.
- [Assessment scope](templates/assessment-scope.xlsx): your applicable requirements, decisions and rationale.

## Start using a tracker

Download a file and keep your working copy private. Record your organization and scope near the top, then fill the pale-yellow input cells. Risk score cells are calculated. Add rows inside the table and check formulas and ranges when extending it. Excel is the intended format; Google Sheets import and round-trip behavior have not been verified.

The files contain no complete ISO, SOC 2, GDPR, Saudi or UAE requirement catalogue. They do not verify controls or certify compliance. Add only content you have rights to use.

## Use and support

The six original trackers are [MIT licensed](LICENSE). You can use, modify and redistribute them, including commercially, while retaining the notice. Application code, brand/logo rights and third-party standards are not included. See [usage notes](templates/TERMS.txt).

Need a scoped, human-reviewed gap assessment? [Visit ABZSECURE](https://abzsecure.com/) or email contact@abzsecure.com. Scope and fees are agreed before work begins.

## Contribute safely

Suggest clearer fields or report reproducible formula issues. Never attach completed customer files, credentials or personal data to issues. Share a fictional example instead. See [contribution guidance](CONTRIBUTING.md).

## A practical first week

1. Agree one business scope and assign a reviewer.
2. Record requirements you have rights to use in Assessment scope.
3. Log missing evidence in Evidence register; keep file references private.
4. Record material risks with an owner and an agreed scoring method.
5. Give each gap a remediation owner and deadline.
6. Review the records and update decisions. A filled workbook is not evidence of compliance.

## Verification

CI checks the six expected XLSX files, their recorded SHA-256 hashes, ZIP/XML structure, prepared data ranges, validation and absence of macros/external workbook links. It does not run Microsoft Excel or prove every formula's behavior. The release's artifact-tool checks covered rendering and representative blank/changed-input formulas; native Excel and Google Sheets round trips remain unverified.

## Scope and privacy

Keep filled-in copies in your organization's approved storage. Do not commit completed trackers here. This repository contains no GRC backend, customer records, evidence attachments or copied framework library.
