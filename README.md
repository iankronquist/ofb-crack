OFB Crack: Breaking OFB Mode with Oracles
=========================================

OFB Mode is a cipher text chaining mode which when used alone without any sort
of Message Authentication code is vulnerable to a Chosen Ciphertext Attack
(CCA).

Deficiencies:
* OFB Mode, even when properly implemented, is not secure against a chosen
  ciphertext attack (CCA). In fact, demonstrating that is the whole point of
  this project.
* The PRF I implement is laughable. I am open to suggestions.
* There are probably many subtle bugs which render this insecure anyhow.

Novel attacks against this purposefully insecure system are welcome! In fact,
all PRs are.
