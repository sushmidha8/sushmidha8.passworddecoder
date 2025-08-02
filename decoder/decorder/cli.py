import argparse
from .decoder import PasswordDecoder

def main():
    parser = argparse.ArgumentParser(description="Decode ASCII-encoded passwords.")
    parser.add_argument("passwords", nargs="+", help="Space-separated ASCII values (e.g., '104 101 108 108 111')")
    args = parser.parse_args()

    decoder = PasswordDecoder()
    
    print("🔓 Password Decoder 🔓")
    print("----------------------")
    
    for pwd in args.passwords:
        result = decoder.decode(pwd)
        print(f"🔢 Encoded: {pwd}")
        print(f"🔓 Decoded: {result if result else '❌ Invalid input!'}")
        print("---")
    
    stats = decoder.get_stats()
    print(f"📊 Stats: {stats['total_attempts']} decoded | Success: {stats['success_rate']}")

if __name__ == "__main__":
    main()