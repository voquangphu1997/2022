def find_max_number_and_remove_it_from_list(lis):
    max_lis = max(lis)
    lis.remove(max_lis)
    return max_lis

lis = [1, 0, 5, 6,8, 7, 65]

first_best_score =  find_max_number_and_remove_it_from_list(lis)
sencond_best_score =  find_max_number_and_remove_it_from_list(lis)

print("first best score: " + str(first_best_score))
print("sencond best score: " + str(sencond_best_score))
