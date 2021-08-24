from ed_post import EdPost


def main():
    post1 = EdPost('Typo in spec?', 'Assignment 1')
    post1.add_comment('There was a typo!')
    post1.add_comment('And maybe another typo?')
    
    post2 = EdPost("What's Hunter's favorite dog?")
    post2.add_comment("There can't be just one!")
    
    post1.display()
    print()
    post2.display()

    
if __name__ == '__main__':
    main()
