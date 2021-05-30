def get_generation(cells, generations):
    output_cells = cells[0][0] #[Y][X]
    return output_cells

def main():
    start = [[1,0,0],
            [0,1,1],
            [1,1,0]]
    print(get_generation(start, 1))

if __name__ == '__main__':
    main()