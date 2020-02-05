'''
Question 2:
A square grid of satellites receive periodic updates. When a satellite receives an update it can update other
satellites directly adjacent to it that have not yet received the update. When a satellite receives a new update
it can update its adjacent neighbors the following day. Write a program to update a square grid of satellites
and determine how many days it will take to update all satellites in the grid. Satellites with updates will be
indicated with a 1 and satellites without the update a 0. If the grid cannot be fully updated return -1.
'''

class satellite(object):
    def __init__(self, grid, row, column):
        self.row           = row
        self.column        = column
        self.sat_grid_dict = self._makeSatGridDict(grid)

    def _makeSatGridDict(self, grid):
        ''' Create the master list of satellites with info about each '''
        sat_grid_dict  = {}
        position_count = 0

        for sub_list in grid:
            for item in sub_list:
                sat_grid_dict[position_count] = {   'Status'          : item,
                                                    'UpdatedToday'    : False,
                                                    'UpdateOperations': self._findUpdateOperations(position_count),
                                            }
                position_count += 1
        return sat_grid_dict

    def _findUpdateOperations(self, current_position):
        ''' Find the positions that can be updated for the position being passed through '''
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

    def _updatePosition(self, item, positions_updated):
        ''' Pass on the update to eligible satellites '''
        position   = item[0]
        operations = item[1].get('UpdateOperations')

        for op in operations:
            update_candidate = self.sat_grid_dict.get(position + op)
            if update_candidate.get('Status') == 0 and not update_candidate.get('UpdatedToday'):
                self.sat_grid_dict[position + op]['Status']       = 1
                self.sat_grid_dict[position + op]['UpdatedToday'] = True
                positions_updated += 1
        return positions_updated

    def updateSatellite(self):
        ''' Iterate through the list of satellites and pass off satelittes that can update others '''
        positions_updated = 0
        for item in self.sat_grid_dict.items():
            if item[1].get('Status') == 1 and not item[1].get('UpdatedToday'):
                positions_updated = self._updatePosition(item, positions_updated)
        return positions_updated

    def resetDay(self):
        ''' Reset the UpdatedToday value for all satellites at the end of the day '''
        for item in self.sat_grid_dict:
            self.sat_grid_dict[item]['UpdatedToday'] = False

    def printGrid(self, days):
        ''' Prints the grid in the terminal with its updates for the day '''
        print('Day {0}'.format(days))
        row = []
        for item in self.sat_grid_dict.items():
            if item[0] % self.column == 0 and item[0] != 0:
                print(row)
                row = []
            row.append(item[1]['Status'])
        print('{0}\n'.format(row))

    def runUpdatingSequence(self, print_grid = True):
        ''' Main run to update all satellites in the grid '''
        days = 0
        if print_grid: self.printGrid(days)

        while self.updateSatellite() > 0:
            days += 1
            if print_grid: self.printGrid(days)
            self.resetDay()

        if days == 0:
            return -1
        return days


if __name__ == '__main__':
    g=[[ 0, 0, 0, 1],
       [ 0, 0, 0, 0],
       [ 0, 1, 0, 0],
       [ 0, 0, 0, 0],]

    s = satellite(g, 4, 4)
    num_days = s.runUpdatingSequence()
    print('Number of days to update all the satellites was {0}'.format(num_days))