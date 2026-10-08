# Hack The Box: Redeemer

**Focus:** Redis service enumeration and key-value data inspection  
**Environment:** Authorised Hack The Box training lab  
**Level:** Beginner study notes

## Goal

I used this exercise to learn the basics of Redis and practise inspecting a database service that was reachable in the lab.

## My approach

1. I checked connectivity to the target running in my authorised HTB lab.
2. I used Nmap service detection to identify exposed services.
3. The scan showed Redis listening on TCP port 6379.
4. I installed the Redis command-line client tools and connected to the lab service.
5. I inspected the server information, checked the available database/keyspace information and selected database 0.
6. I listed the keys and retrieved the relevant value needed to complete the exercise.
7. I submitted the lab flag through Hack The Box. The flag and any target-specific secrets are omitted from this public note.

## Commands and concepts

Use the IP address assigned to your own authorised lab instance.

```bash
ping <TARGET_IP>
nmap -sV -p 6379 <TARGET_IP>
sudo apt install redis-tools
redis-cli -h <TARGET_IP>
```

Inside the Redis CLI, the main commands covered were:

```text
INFO
SELECT 0
KEYS *
GET <key>
```

`INFO` returns server and database statistics. `SELECT 0` switches to database index 0. `KEYS *` lists keys in the selected database, while `GET` retrieves a string value for a specific key. In production, avoid broad `KEYS *` queries on large databases; use safer approaches appropriate to the environment.

## What I learned

- Redis is a key-value data store often used for fast data access and caching.
- A reachable Redis port deserves careful review; exposure should be intentional.
- Authentication, network boundaries and command permissions determine who can inspect or change data.
- Enumeration should be methodical: identify the service, understand the database context and then inspect only what is necessary.

## Defensive takeaway

Do not expose Redis directly to untrusted networks. Bind it to trusted interfaces, apply firewall rules, configure authentication and access controls, keep the service updated and monitor access. Treat cached or temporary data as potentially sensitive.

## Reflection

This exercise helped me connect port enumeration to service-specific investigation. It also reminded me that a database service should be protected by both network controls and appropriate application-level access restrictions.
