file = open("part2.txt", 'r')
priests = int(file.readlines()[0][:-1])
file.close()

acolytes = 1111
available_blocks = 20240000

def build_tower(available_blocks: int) -> tuple[int, int]:
    """_summary_

    Args:
        available_blocks (int): available blocks

    Returns:
        tuple[int,int]: first value is additional blocks needed to complete the tower, second value is width of the tower
    """
    
    thickness = 1 # layer 1 has always thickness equal to 1
    layers = 1 # there's always a starting layer
    width = 1
    n = available_blocks
    
    #print(f"layer                   thickness")
    while n - thickness * width > 0:
        #print(f"{layers=}: ({thickness} * {priests}) mod {acolytes} = {(thickness * priests) % acolytes}; {thickness*width=}; {n=}")
        n -= thickness * width
                
        thickness = (thickness * priests) % acolytes
                
        layers += 1
        width += 2
    
    #print(f"last: {width=} {thickness=}, {n=}")
    
    return [width, thickness*width - n]

a, b = build_tower(available_blocks)
#print(a, b)
print(a*b)