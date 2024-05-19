class LaunderingBusiness:
    def __init__(self,
                owner: str,
                name: str,
                type: str,
                
                launder_limit: int):
        self.owner = owner
        self.name = name
        self.type = type
        self.launder_limit = launder_limit # per month