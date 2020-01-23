def numUniqueEmails(emails):
    duplicate = set()

    for email in emails:
        string = ""
        plus_flag = True
        at_seen = False

        for char in email:
            if char == '@':
                string += char
                plus_flag = True
                at_seen = True
            elif not plus_flag:
                continue
            elif char == '+':
                plus_flag = False
            elif at_seen and char == '.':
                string += char
            elif char == '.':
                continue
            else:
                string += char
        duplicate.add(string)
    return len(duplicate)


def numUniqueEmails(self, emails: List[str]) -> int:
    duplicate = set()

    for email in emails:
        local, domain = email.split('@')
        local_dot = local.split('+')[0]
        domain = '@' + domain
        result = "".join(local_dot.split('.')) + domain
        duplicate.add(result)