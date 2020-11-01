def list_to_str(header, full_list, str_fun=str, separator='\n\t'):
    return header + '\n\t' + separator.join(map(str_fun, full_list))
