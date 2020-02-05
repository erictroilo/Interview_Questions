def threeKeywordSuggestions(repository, customer_query):
    ''' Print out the best keyword suggestions in alphabetical order '''
    # convert all to uppercase so the repository can properly be put in alphabetical order
    repository = [repo_item.upper() for repo_item in repository]
    customer_query = customer_query.upper()
    repository.sort()

    suggestion_list = []
    num_search_chars = len(customer_query)

    for repo_item in repository:
        if customer_query[0:num_search_chars] == repo_item[0:num_search_chars]:
            suggestion_list.append(repo_item)
            if len(suggestion_list) == 3:
                break
    return suggestion_list


if __name__ == '__main__':
    print(threeKeywordSuggestions(['bags', 'baggage', 'banner', 'box', 'clothes', 'baggies'], 'ba'))
    print(threeKeywordSuggestions(['BAGS', 'baggage', 'banner', 'box', 'clothes', 'Baggies'], 'bA'))
    print(threeKeywordSuggestions(['bags', 'baggage', 'banner', 'box', 'clothes', 'baggies'], 'bagg'))