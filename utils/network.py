import socket

class NetworkUtils:
    @staticmethod
    def get_ipv4_address():
        """Get the current IPv4 address of the machine."""
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # Connect to an external server to determine the local IP address
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
        except Exception as e:
            print(f"Error getting IP address: {e}")
            ip = "127.0.0.1"  # fallback to localhost
        finally:
            s.close()
        return ip
