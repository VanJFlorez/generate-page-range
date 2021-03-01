import sys

# USAGE
# py .\main.py slides from_page to_page
def main():
  method = sys.argv[1]
  if method == 'slides':
    slides(int(sys.argv[2]), int(sys.argv[3]))

def slides(beg, end):
  back_pages  = []
  front_pages = []
  i = beg
  full_step = False
  while (i < end  + 1):
    front_pages.append(i)
    if (i + 2 < end + 1):
      back_pages.append(i + 2)
    if (full_step):
      i = i + 2
      full_step = False
    else:
      full_step = True
    i = i + 1
  print(front_pages)
  print(back_pages)
      
if __name__ == "__main__":
  main()