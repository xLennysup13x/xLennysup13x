# Hack The Box: Dancing

**Focus:** SMB enumeration and share permissions  
**Environment:** Authorised Hack The Box training lab  
**Level:** Beginner study notes

## Goal

The goal of this exercise was to learn how to inspect SMB shares and understand what can happen when a share allows access without the expected credentials.

## My approach

1. I checked that the lab target was reachable from my authorised lab connection.
2. I scanned the target to identify available network services and noticed SMB was exposed.
3. I listed the available SMB shares to understand what the server made available.
4. I checked access to the listed shares using the lab's permitted guest/blank-credential approach.
5. The administrative shares denied access, but the custom `WorkShares` share allowed access.
6. I listed the directories, navigated through them and downloaded the lab files needed to complete the exercise.
7. I reviewed the retrieved files locally and submitted the lab flag through Hack The Box. The flag itself is intentionally not included in this public note.

## Commands I used / concepts to remember

Use the live target address assigned to your own HTB instance; do not copy someone else's target IP.

```bash
ping <TARGET_IP>
nmap -sV -p 139,445 <TARGET_IP>
smbclient -L //<TARGET_IP>/ -N
smbclient //<TARGET_IP>/WorkShares -N
```

Inside the SMB client, the commands I used to explore the share were:

```text
ls
cd <directory>
get <filename>
exit
```

Exact results can vary by instance. Run these only against the authorised lab target.

## What I learned

- SMB share enumeration can reveal which folders and resources are exposed.
- Administrative shares and custom shares can have different permissions.
- A share that allows unauthenticated access may expose internal documents or other sensitive information.
- It is important to check the actual permissions rather than assume every share behaves the same way.

## Defensive takeaway

Administrators should disable guest access where it is not required, apply least-privilege permissions to each share, review exposed files and monitor SMB access. Sensitive information should not be stored in broadly accessible locations.

## Reflection

The main lesson for me was to enumerate first and then verify access one share at a time. The result is more useful when I record both the successful access and the denied attempts, because that shows how the permissions differed.
