start_day = int(input().split()[-1])
start_time = list(map(int, input().replace(" ", "").split(":")))

end_day = int(input().split()[-1])
end_time = list(map(int, input().replace(" ", "").split(":")))

start_total_seconds = (start_day * 24 * 3600) + (start_time[0] * 3600) + (start_time[1] * 60) + start_time[2]
end_total_seconds = (end_day * 24 * 3600) + (end_time[0] * 3600) + (end_time[1] * 60) + end_time[2]

total_seconds = end_total_seconds - start_total_seconds

days = total_seconds // (24 * 3600)
total_seconds %= 24 * 3600
hours = total_seconds // 3600
total_seconds %= 3600
minutes = total_seconds // 60
seconds = total_seconds % 60

print(f"{days} dia(s)")
print(f"{hours} hora(s)")
print(f"{minutes} minuto(s)")
print(f"{seconds} segundo(s)")
