# Example PowerShell credential handling — template only
# This file previously contained a hard-coded example password.
# Do not put real passwords, tokens, or credentials in source control.
# Use an approved secret manager or prompt securely at runtime instead.

$username = Read-Host "Username"
$securePassword = Read-Host "Password" -AsSecureString
$credential = [System.Management.Automation.PSCredential]::new($username, $securePassword)

# Add your authorised file/share operation here.
# Validate the target and permissions before connecting.
