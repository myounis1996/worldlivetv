import time
import random


def generate_unlock_code(method='view'):
    """
    Generates an unlock code similar to the one used by the website.

    Parameters:
        method (str): Either 'click' (24h validity) or 'view' (2h validity).

    Returns:
        dict: A dictionary containing the unlock code, URL, and expiration timestamp.
    """
    if method.lower() == 'click':
        validity_hours = 24
        rnd_min, rnd_max = 5, 9
    elif method.lower() == 'view':
        validity_hours = 2
        rnd_min, rnd_max = 0, 4
    else:
        raise ValueError("Invalid method. Use 'click' or 'view'.")
    current_time_ms = int(time.time() * 1000)
    validity_ms = validity_hours * 60 * 60 * 1000
    future_time_ms = current_time_ms + validity_ms
    time_str = str(future_time_ms)
    rnd_digit = str(random.randint(rnd_min, rnd_max))
    modified_code = time_str[:5] + rnd_digit + time_str[5:]
    unlock_url = f"http://worldlivetv.stream?code={modified_code}"

    return {
        'code': modified_code,
        'url': unlock_url,
        'valid_until': future_time_ms
    }


if __name__ == "__main__":
    user_method = input("Enter method (click/view): ").strip().lower()
    if user_method not in ['click', 'view']:
        print("Invalid method. Defaulting to 'view'.")
        user_method = 'view'

    try:
        result = generate_unlock_code(user_method)
        print("\n✅ Unlock Code Generated Successfully!")
        print(f"Code: {result['code']}")
        print(f"URL: {result['url']}")
        print(f"Valid Until: {time.ctime(result['valid_until'] / 1000)}")
    except Exception as e:
        print(f"❌ Error: {e}")