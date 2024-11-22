file = open("part1.txt", 'r')
available_blocks = int(file.readlines()[0][:-1])
file.close()
                                            
def build_tower(available_blocks: int) -> tuple[int, int]:
    """_summary_

    Args:
        available_blocks (int): available blocks

    Returns:
        tuple[int,int]: first value is additional blocks needed to complete the tower, second value is width of the tower
    """
    
    width = 1
    
    n = available_blocks
    while n - width > 0:
        n -= width
        width += 2
    
    return[width, width - n]


a, b = build_tower(available_blocks)
print(a*b)