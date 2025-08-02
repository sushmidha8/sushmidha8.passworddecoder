class PasswordDecoder:
    """Decodes ASCII-based encoded passwords by reversing the values."""
    
    def __init__(self):
        self.total_decoded = 0
        self.successful = 0
    
    def decode(self, encoded_str: str) -> str | None:
        """Decodes a space-separated ASCII string into plaintext."""
        self.total_decoded += 1
        
        try:
            # Split into ASCII numbers, reverse, and convert to chars
            decoded = ''.join([chr(int(num)) for num in encoded_str.split()[::-1]])
            self.successful += 1
            return decoded
        except (ValueError, TypeError):
            return None
    
    def get_stats(self) -> dict:
        """Returns decoding statistics."""
        return {
            "total_attempts": self.total_decoded,
            "success_rate": f"{(self.successful / self.total_decoded) * 100:.1f}%" 
            if self.total_decoded else "0%"
        }