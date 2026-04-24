PI = 3.14

def square(n):
  return n ** 2

def main():
  ans = square(2)
  if(ans == 4):
    print(ans , True)
  else:
    print(ans, False)
  pass

if __name__ == "__main__":
  print("my module is running")
  main()
