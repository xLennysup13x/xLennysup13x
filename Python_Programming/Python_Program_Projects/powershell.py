$Username =  "WIN01\john"
$Password = "SecurePassword123"
$SecurePassword = ConvertTo-SecureString $Password -AsPlainText -Force
$Credential = New-Object System.Management.Automation.PSCredential($Username, $SecurePassword)
                                                                   
$remoteShare = "\\\FileServer01\SharedFolder"
$sourceFileName = Read-Host -Prompt "File>"
$sourceFilePath = ConvertTo-SecureString