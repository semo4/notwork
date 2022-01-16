
class DomainHelper:
    def get_filter_domain(self, domain):
        if domain != 'all':
            return f'python infornito.py history --profile 2 --filter domain={domain}'

        else:
            return f'python infornito.py history --profile 2 --filter'
