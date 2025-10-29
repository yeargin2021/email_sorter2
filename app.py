def sort(emails):
    def email_sort_key(email):
        username, domain = email.split("@")
        return (domain.lower(), username.lower())  # Sort by domain first, then username (case insensitive)
    
    return sorted(emails, key=email_sort_key)


# Test with mixed case emails
# test_emails = ["Jill@Mail.com", "john@EXAMPLE.com", "Jane@example.com", "BOB@example.com"]
# result = sort(test_emails)
# print("Original:", test_emails)
# print("Sorted:", result)
