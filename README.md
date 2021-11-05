# mfa-appointment-checker
Simple crawler to check for available slots at online.mfa.gov.ua/application.
The script sends slack notification if there are any available slots found

# Execute
Set slack tocken and chanel id:
```python
slack_token = 'YOUR_TOKEN'
slack_channel = 'YOUR_CHANEL_ID'
```

Set a cron job to execute the script every few minutes
```bash
python mfa.py
```

There was a capcha added to online.mfa.gov.ua so the script does not work anymore.
The repository has been moved to the archive.
