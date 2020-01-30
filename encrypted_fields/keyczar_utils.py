import base64


def Base64WSEncode(s):
  """
  Return Base64 web safe encoding of s. Suppress padding characters (=).

  Uses URL-safe alphabet: - replaces +, _ replaces /. Will convert s of type
  unicode to string type first.

  @param s: bytes to encode as Base64
  @type s: bytes

  @return: Base64 representation of s.
  @rtype: bytes
  """
  return base64.urlsafe_b64encode(s).replace(b"=", b"")


def Base64WSDecode(s):
  """
  Return decoded version of given Base64 string. Ignore whitespace.

  Uses URL-safe alphabet: - replaces +, _ replaces /. Will convert s of type
  unicode to string type first.

  @param s: Base64 string to decode
  @type s: string

  @return: original string that was encoded as Base64
  @rtype: bytes

  @raise Base64DecodingError: If length of string (ignoring whitespace) is one
    more than a multiple of four.
  """
  s = ''.join(s.splitlines())
  b = s.replace(" ", "").encode('ascii')  # kill whitespace, make string (not unicode)
  d = len(b) % 4
  if d == 1:
    raise ValueError('Base64DecodingError')
  elif d == 2:
    b += b"=="
  elif d == 3:
    b += b"="
  try:
    return base64.urlsafe_b64decode(s)
  except TypeError:
    # Decoding raises TypeError if s contains invalid characters.
    raise ValueError('Base64DecodingError')