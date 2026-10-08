# Hack The Box: Fawn

**Focus:** FTP service enumeration and anonymous access  
**Environment:** Authorised Hack The Box training lab  
**Level:** Beginner study notes

## Goal

This lab helped me understand how FTP works and how an incorrectly configured service may allow users to browse or download files without a named account.

## My approach

1. I checked connectivity to the HTB target from the authorised lab connection.
2. I used a service scan to find open ports and identify the FTP service on port 21.
3. I connected to the FTP service and checked whether anonymous login was enabled.
4. The lab allowed the anonymous account to log in, so I listed the available directory contents.
5. I downloaded the lab file needed for the exercise and reviewed it locally.
6. I submitted the flag to the Hack The Box platform. I have not included the flag in this public write-up.

## Commands and notes

Use only the IP address assigned to your own lab instance.

```bash
ping <TARGET_IP>
nmap -sV -p 21 <TARGET_IP>
ftp <TARGET_IP>
```

At the FTP prompt, the lab's anonymous login flow was:

```text
Name: anonymous
Password: <press Enter or follow the lab prompt>
```

Useful FTP commands used in the exercise:

```text
help
ls
get <filename>
bye
```

The server's configuration determines whether anonymous login is permitted and which files that account can access.

## What I learned

- Port 21 is commonly used for FTP, but a port scan alone does not prove how access is configured.
- Anonymous FTP may be useful for legitimate public downloads, but it becomes a risk when it exposes files that should be private.
- Traditional FTP does not encrypt credentials and file contents by default.
- Checking the service version and access behaviour helps build an accurate picture of the service.

## Defensive takeaway

Disable anonymous access unless it is genuinely required. If public file transfer is needed, limit the accessible directory and permissions. Prefer a secure transfer option such as SFTP or properly configured FTPS when confidentiality is required, and avoid placing sensitive files in public transfer folders.

## Reflection

This lab showed me that the next step after identifying a service is to test its access controls carefully and record what is actually permitted, rather than making assumptions based on the service name.
