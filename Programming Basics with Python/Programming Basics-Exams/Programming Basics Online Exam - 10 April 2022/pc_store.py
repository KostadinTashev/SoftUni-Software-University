processor_price = float(input()) * 1.57
video_card_price = float(input()) * 1.57
ram_memory_price = float(input()) * 1.57
count_ram_memory = int(input())
percent_discount = float(input())
total_price_ram_leva = ram_memory_price * count_ram_memory
processor_discount = processor_price - (processor_price * percent_discount)
video_card_discount = video_card_price - (video_card_price * percent_discount)
total_price = processor_discount + video_card_discount + total_price_ram_leva
print(f"Money needed - {total_price:.2f} leva.")
