total_pages = int(input("Total number of pages for read: "))
read_pages_per_hour = int(input("How many pages you can read per hour: "))
days = int(input("For how many days you need to read the book: "))

hours_by_book = total_pages / read_pages_per_hour
needed_hours_per_day = hours_by_book / days

print(f'You need to read {(int(needed_hours_per_day))} hours every day to complete your book in time')
