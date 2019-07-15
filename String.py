class String:

    @classmethod
    def is_palindrome(cls, s, case_insensitive=True):
        s = cls._strip_string(s)
        if case_insensitive:
            s = s.lower()
        return cls._is_palindrome(s)

    @staticmethod
    def _strip_string(s):
        return ''.join(s for c in s if c.isalnum())

    @staticmethod
    def _is_palindrome(s):
        for c in range(len(s)):
            if s[c] != s[-c - 1]:
                return False
        return True


if __name__ == '__main__':
    print(String.is_palindrome('This is a test'))
