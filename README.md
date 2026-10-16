<p align="center"><img src="docs/banner.png" alt="GRC Starter Templates" width="900"></p>

<p align="center">
  <a href="https://abdullahzarshaid.github.io/abzsecure-grc-templates/"><img src="https://img.shields.io/badge/Browse%20online-pick%20a%20tracker-0f766e?style=for-the-badge" alt="Browse online"></a>
  &nbsp;
  <a href="https://github.com/abdullahzarshaid/abzsecure-grc-templates/archive/refs/heads/main.zip"><img src="https://img.shields.io/badge/Download-all%20six%20(.zip)-14314a?style=for-the-badge" alt="Download all"></a>
  &nbsp;
  <a href="https://abdullahzarshaid.com/"><img src="https://img.shields.io/badge/Author-abdullahzarshaid.com-3f8f5b?style=for-the-badge" alt="Author site"></a>
</p>

[![Template integrity](https://github.com/abdullahzarshaid/abzsecure-grc-templates/actions/workflows/templates.yml/badge.svg)](https://github.com/abdullahzarshaid/abzsecure-grc-templates/actions/workflows/templates.yml)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Templates](https://img.shields.io/badge/templates-6-blue.svg)
![Rows](https://img.shields.io/badge/prepared%20rows-100%20each-blue.svg)
![Macros](https://img.shields.io/badge/macros-none-brightgreen.svg)

**Six original blank Excel trackers for small teams organizing security work in spreadsheets.** Each file has 100 prepared rows, status dropdowns, filters and a frozen header. No macros, no sign-up and no customer records: download a file, fill the pale-yellow input cells and keep your working copy private.

<p align="center"><img src="docs/flow.svg" alt="Scope, evidence, risk, remediation and review" width="900"></p>

## Pick a tracker

<table><tr><td align="center"><a href="templates/risk-register.xlsx"><img src="docs/previews/risk-register.png" width="440" alt="Risk register"><br><b>Risk register</b></a></td><td align="center"><a href="templates/evidence-register.xlsx"><img src="docs/previews/evidence-register.png" width="440" alt="Evidence register"><br><b>Evidence register</b></a></td><td align="center"><a href="templates/remediation-tracker.xlsx"><img src="docs/previews/remediation-tracker.png" width="440" alt="Remediation tracker"><br><b>Remediation tracker</b></a></td></tr><tr><td align="center"><a href="templates/vendor-review.xlsx"><img src="docs/previews/vendor-review.png" width="440" alt="Vendor review"><br><b>Vendor review</b></a></td><td align="center"><a href="templates/policy-register.xlsx"><img src="docs/previews/policy-register.png" width="440" alt="Policy register"><br><b>Policy register</b></a></td><td align="center"><a href="templates/assessment-scope.xlsx"><img src="docs/previews/assessment-scope.png" width="440" alt="Assessment scope"><br><b>Assessment scope</b></a></td></tr></table>

- **[Risk register](templates/risk-register.xlsx)**: Risks with owner, treatment and an organization-defined likelihood x impact score. Columns: Risk ID, Risk description, Owner, Likelihood (1-5), Impact (1-5), Score, Treatment, Status, Review date, Notes.
- **[Evidence register](templates/evidence-register.xlsx)**: Evidence requests, file references, reviewers and expiry dates. Columns: Evidence ID, Evidence description, Control / requirement, Owner, File reference, Collected date, Expiry date, Reviewer, Status, Notes.
- **[Remediation tracker](templates/remediation-tracker.xlsx)**: Gaps and actions with owner, priority, deadline and completion evidence. Columns: Action ID, Gap / action, Requirement, Owner, Priority, Due date, Status, Completion evidence, Reviewer, Notes.
- **[Vendor review](templates/vendor-review.xlsx)**: Third-party due diligence, data handled and follow-up actions. Columns: Vendor ID, Vendor name, Service, Data handled, Business owner, Review due, Status, Review evidence, Follow-up action, Notes.
- **[Policy register](templates/policy-register.xlsx)**: Policies with version, approver, approval and next review dates. Columns: Policy ID, Policy title, Owner, Version, Document reference, Approval date, Next review, Status, Approver, Notes.
- **[Assessment scope](templates/assessment-scope.xlsx)**: Applicable requirements, decisions, evidence references and rationale. Columns: Item ID, Requirement / question, Source / version, Applicability, Owner, Decision, Evidence reference, Reviewer, Review date, Rationale.

Row 1 in each preview is a fictional example for orientation. The downloadable files are blank. The six files, `checksums.json` and a zip of all six are also attached to the [latest release](https://github.com/abdullahzarshaid/abzsecure-grc-templates/releases/latest), so a fixed version can be linked from a policy or a procedure.

## How the six connect

<p align="center"><img src="docs/workflow.png" alt="How the six trackers connect" width="900"></p>

Assessment scope decides what applies. The evidence register records what proves it. The risk register holds what remains exposed, scored with your own 1-5 likelihood and impact definitions. The remediation tracker assigns every gap an owner, a deadline and completion evidence. Vendor reviews and the policy register feed those four. Review is a decision you revisit, not a tab you fill once.

## Start using a tracker

Download a file and keep your working copy private. Record your organization and scope near the top, then fill the pale-yellow input cells. Risk score cells are calculated. Add rows inside the table and check formulas and ranges when extending it. Excel is the intended format; Google Sheets import and round-trip behaviour have not been verified.

The files contain no complete ISO 27001, SOC 2, GDPR, Saudi or UAE requirement catalogue. They do not verify controls or certify compliance. Add only content you have rights to use.

## A practical first week

1. Agree one business scope and assign a reviewer.
2. Record requirements you have rights to use in Assessment scope.
3. Log missing evidence in the Evidence register; keep file references private.
4. Record material risks with an owner and an agreed scoring method.
5. Give each gap a remediation owner and deadline.
6. Review the records and update decisions. A filled workbook is not evidence of compliance.

## Verification

CI checks the six expected XLSX files, their recorded SHA-256 hashes, ZIP/XML structure, prepared data ranges, validation and absence of macros or external workbook links. It does not run Microsoft Excel or prove every formula's behaviour. Native Excel and Google Sheets round trips remain unverified.

## Use and support

The six original trackers are [MIT licensed](LICENSE). You can use, modify and redistribute them, including commercially, while retaining the notice. Brand and logo rights and third-party standards are not included. See the [usage notes](templates/TERMS.txt).

Questions about a template: open an issue here or email abdullahbinzarshaid@gmail.com. A scoped, human-reviewed gap assessment is offered through [ABZSECURE](https://abzsecure.com/); scope and fees are agreed before work begins.

## Contribute safely

Suggest clearer fields or report reproducible formula issues. Never attach completed customer files, credentials or personal data to issues. Share a fictional example instead. See the [contribution guidance](CONTRIBUTING.md).

## Scope and privacy

Keep filled-in copies in your organization's approved storage. Do not commit completed trackers here. This repository contains no GRC backend, customer records, evidence attachments or copied framework library.
