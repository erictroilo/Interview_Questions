def threeKeywordSuggestions(repository, customerQuery):
    # convert all to uppercase so the repository can properly be put in alphabetical order
    repository = [repo_item.upper() for repo_item in repository]
    customerQuery = customerQuery.upper()
    repository.sort()

    suggestion_list = []
    num_search_chars = len(customerQuery)

    for repo_item in repository:
        if customerQuery[0:num_search_chars] == repo_item[0:num_search_chars]:
            suggestion_list.append(repo_item)
            if len(suggestion_list) == 3:
                break
    return suggestion_list

print( threeKeywordSuggestions(['bags', 'baggage', 'banner', 'box', 'clothes', 'baggies'], 'ba') )




class satellite(object):
    def __init__(self, grid, row, column):
        self.grid        = grid
        self.row         = row
        self.column      = column
        self.master_dict = self.make_master_dict(grid)

    def make_master_dict(self, grid):
        master_dict = {}
        position_count = 0

        for sub_list in grid:
            for item in sub_list:
                master_dict[position_count] = {   'Status'          : item,
                                                  'UpdatedToday'    : False,
                                                  'UpdateOperations': self.findPositionType(position_count),
                                            }
                position_count += 1
        return master_dict

    def findPositionType(self, current_position):
        position = current_position + 1
        remainder = current_position % self.column

        # top left corner
        if position == 1:
            return (1, self.column)
        # bottom right corner
        elif position == (self.row * self.column):
            return (-1, -1*self.column)
        # top right corner
        elif position == self.column:
            return (-1, self.column)
        # bottom left corner
        elif position == ((self.row * (self.column - 1)) + 1):
            return (1, -1*self.column)
        # top row middle
        elif position > 1 and position < self.column:
            return (-1, 1, self.column)
        # bottom row middle
        elif position > (self.row * (self.column - 1)) and position < (self.row * self.column):
            return (-1, 1, -1*self.column)
        #left column middle
        elif remainder == 0:
            return(1, self.column, -1*self.column)
        # right column middle
        elif remainder == (self.column - 1):
            return(-1, self.column, -1*self.column)
        # middle
        elif remainder > 0 and remainder < (self.column - 1):
            return (-1, 1, self.column, -1 * self.column)

    def updatePositions(self, item, positions_updated):
        position = item[0]
        operations = item[1].get('UpdateOperations')

        for op in operations:
            update_candidate = self.master_dict.get(position + op)
            if update_candidate.get('Status') == 0 and not update_candidate.get('UpdatedToday'):
                self.master_dict[position + op]['Status']       = 1
                self.master_dict[position + op]['UpdatedToday'] = True
                positions_updated += 1
        return positions_updated

    def updateSatellite(self):
        positions_updated = 0
        for item in self.master_dict.items():
            if item[1].get('Status') == 1 and not item[1].get('UpdatedToday'):
                positions_updated = self.updatePositions(item, positions_updated)
        return positions_updated

    def resetDay(self):
        for item in self.master_dict:
            self.master_dict[item]['UpdatedToday'] = False

    def printGrid(self, days):
        print('Day {0}'.format(days))
        row = []
        for item in self.master_dict.items():
            if item[0] % self.column == 0 and item[0] != 0:
                print(row)
                row = []
            row.append(item[1]['Status'])
        print('{0}\n'.format(row))

    def runUpdatingSequence(self, print_on = True):
        days = 0
        while self.updateSatellite() > 0:
            days += 1
            if print_on:
                self.printGrid(days)
            self.resetDay()
        return days


g=[[ 0, 0, 0, 1],
   [ 0, 0, 0, 0],
   [ 0, 1, 0, 0],
   [ 0, 0, 0, 0],]

s = satellite(g, 4, 4)
num_days = s.runUpdatingSequence()
print('Number of days to update all the satellites was {0}'.format(num_days))


