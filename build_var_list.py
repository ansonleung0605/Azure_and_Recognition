# Build a Variable List of Adjacent Cells
def build_var_list(row, col, VARS):
    var_list = []
 
    idx = row*n + col
    var_list.append(VARS[idx])

    idx_right = row*n + col+1
    idx_left = row*n + col-1

    idx_down = (row+1)*n + col
    idx_up = (row-1)*n + col

    idx_right_down = (row+1)*n + col+1
    idx_left_down = (row+1)*n + col-1

    idx_left_up = (row-1)*n + col-1
    idx_right_up = (row-1)*n + col+1

    if row == 0:
        var_list.append(VARS[idx_down])
        if col == 0:
            var_list.append(VARS[idx_right])
            var_list.append(VARS[idx_right_down])
        elif col == n-1:
            var_list.append(VARS[idx_left_down])
            var_list.append(VARS[idx_left])
        else:
            var_list.append(VARS[idx_right])
            var_list.append(VARS[idx_right_down])
            var_list.append(VARS[idx_left_down])
            var_list.append(VARS[idx_left])
    elif row == n-1:
        var_list.append(VARS[idx_up])
        if col == 0:
            var_list.append(VARS[idx_right_up])
            var_list.append(VARS[idx_right])
        elif col == n-1:
            var_list.append(VARS[idx_left])
            var_list.append(VARS[idx_left_up])
            pass
        else:
            var_list.append(VARS[idx_right_up])
            var_list.append(VARS[idx_right])
            var_list.append(VARS[idx_left])
            var_list.append(VARS[idx_left_up])
    else:
        var_list.append(VARS[idx_down])
        var_list.append(VARS[idx_up])
        if col == 0:
            var_list.append(VARS[idx_right_up])
            var_list.append(VARS[idx_right])
            var_list.append(VARS[idx_right_down])
        elif col == n-1:
            var_list.append(VARS[idx_left])
            var_list.append(VARS[idx_left_up])
            var_list.append(VARS[idx_left_down])
        else:
            var_list.append(VARS[idx_right_up])
            var_list.append(VARS[idx_right])
            var_list.append(VARS[idx_right_down])
            var_list.append(VARS[idx_left])
            var_list.append(VARS[idx_left_up])
            var_list.append(VARS[idx_left_down])

    return var_list