import copy

class Matrix:
    def __init__(self, data):
        self.rows, self.cols, self.rotations = map(int, data[0].strip().split(' '))
        self.num_rings = int(min(self.rows, self.cols) / 2)
        self.elms = []
        for row_index in range(self.rows):
            self.elms.extend(list(map(int, data[1 + row_index].strip().split(' '))))

    def get_ring_definition(self, ring_index):
        ring_length = self.cols - (ring_index * 2)
        ring_height = self.rows - (ring_index * 2)
        return ring_length, ring_height, ring_length * 2 + (ring_height - 2) * 2

    def get_ring_elm_index(self, ring_index, elm_index):
        ring_length, ring_height, ring_size = self.get_ring_definition(ring_index)
        start_index = ring_index * self.cols + ring_index
        if elm_index > ring_size - ring_length:
            return start_index + (ring_size - elm_index)  # top
        elif ring_height <= elm_index <= ring_height + ring_length - 2:
            return start_index + self.cols * (ring_height - 1) + (elm_index - (ring_height - 1))  # bottom
        elif elm_index < ring_height:
            return start_index + self.cols * elm_index  # left
        elif elm_index > (ring_height + ring_length) - 2:
            return start_index + self.cols * ((ring_size - elm_index) - (ring_length - 1)) + (ring_length - 1)  # right

    def rotate(self):
        new_elms = copy.deepcopy(self.elms)
        for ring_index in range(self.num_rings):
            _, _, ring_size = self.get_ring_definition(ring_index)
            for elm_index in range(ring_size):
                ring_elm_index = self.get_ring_elm_index(ring_index, elm_index)
                val = self.elms[ring_elm_index]
                ring_elm_index = self.get_ring_elm_index(ring_index, (elm_index + self.rotations) % ring_size)
                new_elms[ring_elm_index] = val
        self.elms = new_elms
        for row_index in range(self.rows):
            for col_index in range(self.cols):
                print(self.elms[col_index + row_index * self.cols], end=' ')
            print()

input_1 = ['4 4 2',
           '1 2 3 4',
           '5 6 7 8',
           '9 10 11 12',
           '13 14 15 16']

input_2 = ['5 4 7',
           '1 2 3 4',
           '7 8 9 10',
           '13 14 15 16',
           '19 20 21 22',
           '25 26 27 28']

input_3 = ['2 2 3',
           '1 1',
           '1 1']


Matrix(input_1).rotate()
print()
Matrix(input_2).rotate()
print()
Matrix(input_3).rotate()
