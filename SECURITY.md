# Security and prototype scope

Use localhost and synthetic documents only. This is not a production service.

Known limits: demo-role headers are not authentication; the encrypted vault key is process-local and cannot recover older blobs after restart; rights/deletion scheduling, backup expiry and key management are incomplete. Registry/DigiLocker/e-sign/payment/serviceability calls are mocks. No-GST final evidence is pending. Current tests do not establish that an uploader is the lawful owner of a document.

Never upload real identity documents, funds or credentials. Do not expose this app publicly without implementing those controls.

For a vulnerability, contact the repository maintainer privately using an available GitHub private-reporting channel. Do not place exploit data, tokens or personal documents in a public issue. See [the privacy design](docs/PRIVACY.md) and [the identity-binding regression](evaluation/identity_binding_regression.md).
