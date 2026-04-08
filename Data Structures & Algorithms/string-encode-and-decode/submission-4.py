class Solution:
        hashCode = "DFKSFSDNFSDNFJSKDJFNSDJNFJDSNJKNFJKSNDJKFNSDJKNFJKSN"
        hashCode1 = "DFKSFSDNFSDNFJSKDJFNSDJNFJDSNJKNFJKSNDJKFNSDJKNF"
        
        def encode(self, strs: List[str]) -> str:
                if strs == []:
                        return self.hashCode1
                return self.hashCode.join(strs)
        def decode(self, s: str) -> List[str]:
                print(s)
                if s == self.hashCode1:
                        return []
                return s.split(self.hashCode)