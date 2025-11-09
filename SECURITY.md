# Security Policy

## Security Overview

This document outlines the security measures implemented in the BMI Calculator application and provides guidance for maintaining security.

## Recent Security Fixes (2024-11-09)

### Critical Fixes Implemented

1. **XSS Vulnerability Mitigation**
   - **Issue**: Unsafe HTML rendering with `unsafe_allow_html=True`
   - **Fix**: Replaced all unsafe HTML with Streamlit native components (st.metric, st.success, st.warning, st.error, st.info)
   - **Impact**: Eliminates potential XSS attack vectors

2. **Error Handling**
   - **Issue**: No error handling for calculations and user inputs
   - **Fix**: Added comprehensive try-except blocks with logging
   - **Impact**: Prevents application crashes and provides audit trail

3. **Input Validation**
   - **Issue**: Limited validation of user inputs
   - **Fix**: Added validation in `calculate_bmi()` function
   - **Impact**: Rejects unrealistic values (height >300cm, weight >500kg, negative values)

4. **Dependency Management**
   - **Issue**: Bloated requirements.txt with transitive dependencies
   - **Fix**: Separated direct dependencies (requirements.txt) from locked versions (requirements-lock.txt)
   - **Impact**: Easier to update and audit dependencies

## Security Measures

### Input Validation
All user inputs are validated before processing:
- Height: 0-300 cm (rejects negative and unrealistic values)
- Weight: 0-500 kg (rejects negative and unrealistic values)
- BMI: Cannot be negative

### Error Handling
- All calculations wrapped in try-except blocks
- Errors logged with full context
- User-friendly error messages displayed
- Application fails gracefully without exposing internals

### Logging
- All user actions logged for audit trail
- Error logs include timestamps and context
- Log files are rotated (max 10MB, 5 backups)
- Logs excluded from version control (.gitignore)

### Data Security
- No sensitive data collected or stored
- No database or file system writes (except logs)
- No network requests to external services
- All data processing happens in memory

## Dependency Security

### Checking for Vulnerabilities

Install security tools:
```bash
pip install safety bandit
```

### Check Dependencies for Known Vulnerabilities
```bash
safety check --file requirements-lock.txt
```

Run this regularly or integrate into CI/CD pipeline.

### Static Security Analysis
```bash
bandit -r app.py
```

Bandit scans for common security issues in Python code.

### Updating Dependencies

1. Check for updates:
```bash
pip list --outdated
```

2. Update requirements.txt with new version ranges:
```txt
streamlit>=1.41.0,<2.0.0
```

3. Regenerate lock file:
```bash
pip install -r requirements.txt
pip freeze > requirements-lock.txt
```

4. Run security check:
```bash
safety check --file requirements-lock.txt
```

## Security Best Practices

### For Developers

1. **Never commit secrets**
   - No API keys, passwords, or tokens in code
   - Use environment variables for configuration
   - Add sensitive files to .gitignore

2. **Validate all inputs**
   - Never trust user input
   - Use type hints and validate ranges
   - Sanitize data before processing

3. **Handle errors gracefully**
   - Don't expose stack traces to users
   - Log errors for debugging
   - Provide helpful error messages

4. **Keep dependencies updated**
   - Review security advisories regularly
   - Update dependencies promptly
   - Test after updates

5. **Review code changes**
   - Use pull requests for all changes
   - Have security-focused code reviews
   - Run security scans in CI/CD

### For Deployment

1. **Use HTTPS**
   - Never deploy over plain HTTP
   - Use valid SSL certificates
   - Enable HSTS headers

2. **Set security headers**
```python
# In Streamlit config
[server]
enableCORS = false
enableXsrfProtection = true
```

3. **Limit access**
   - Use authentication if needed
   - Restrict by IP if possible
   - Implement rate limiting

4. **Monitor logs**
   - Set up log monitoring
   - Alert on errors
   - Review logs regularly

5. **Regular security audits**
   - Run `safety check` weekly
   - Run `bandit` on code changes
   - Review access logs

## Reporting Security Vulnerabilities

If you discover a security vulnerability, please:

1. **DO NOT** open a public issue
2. Email the maintainer directly with:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

We will respond within 48 hours and provide updates on the fix timeline.

## Security Checklist for Production

- [ ] HTTPS enabled with valid certificate
- [ ] Error handling implemented for all user inputs
- [ ] Input validation in place
- [ ] Logging configured and monitored
- [ ] Dependencies scanned for vulnerabilities
- [ ] Security headers configured
- [ ] Authentication implemented (if needed)
- [ ] Rate limiting enabled (if public)
- [ ] Regular security updates scheduled
- [ ] Incident response plan documented

## Known Limitations

1. **No authentication**: Application is open to anyone with the URL
2. **No rate limiting**: Users can submit unlimited requests
3. **Client-side processing**: All calculations happen in the browser
4. **No data persistence**: No database or storage layer

These are acceptable for a simple calculator but should be addressed for production deployments handling sensitive data.

## Compliance

This application:
- Does not collect personally identifiable information (PII)
- Does not store user data
- Does not use cookies (except Streamlit session state)
- Does not make external API calls

For HIPAA or GDPR compliance, additional measures would be required:
- Data encryption at rest and in transit
- Access logging and audit trails
- User consent mechanisms
- Data retention policies

## Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Python Security Best Practices](https://python.readthedocs.io/en/latest/library/security_warnings.html)
- [Streamlit Security](https://docs.streamlit.io/knowledge-base/deploy/authentication)
- [Safety Documentation](https://pyup.io/safety/)
- [Bandit Documentation](https://bandit.readthedocs.io/)

## Version History

### v1.0.0 (2024-11-09)
- Initial security hardening
- XSS vulnerability fixes
- Error handling implementation
- Input validation
- Dependency security improvements
