import time
from ..decoder.decoder import PasswordDecoder

def benchmark():
    decoder = PasswordDecoder()
    test_passwords = ["104 101 108 108 111", "119 111 114 108 100"] * 5000  # 10k decodes
    
    start = time.time()
    for pwd in test_passwords:
        decoder.decode(pwd)
    elapsed = time.time() - start
    
    stats = decoder.get_stats()
    print(f"⏱️  Decoded {stats['total_attempts']} passwords in {elapsed:.2f}s")
    print(f"🚀 Speed: {stats['total_attempts'] / elapsed:.0f} passwords/sec")
    print(f"✅ Success Rate: {stats['success_rate']}")

if __name__ == "__main__":
    benchmark()