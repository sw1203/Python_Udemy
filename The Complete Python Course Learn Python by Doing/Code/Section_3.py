MENU_PROMPT = "'a' 입력 시 영화 추가, 's' 입력 시 모든 영화 보기, 'f' 입력 시 제목으로 영화 찾기, 'q' 입력 시 종료: "
movies = []


def add_movies():
    title = input("영화 제목: ")
    director = input("영화 감독: ")
    year = input("영화 년도: ")
    movies.append({
        "title": title,
        "director": director,
        "year": year
    })


def show_movies():
    for movie in movies:
        print_movie(movie)


def print_movie(movie):
    print(f"Title : {movie['title']}, Director: {movie['director']}, Year: {movie['year']}")


def find_movie():
    search_title = input("찾고 싶은 영화 제목:")
    for movie in movies:
        if movie['title'] == search_title:
            print_movie(movie)


user_menu = {
    'a': add_movies,
    's': show_movies,
    'f': find_movie,
}


def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection in user_menu:
            select_function = user_menu[selection]
            select_function
        else:
            print("잘못된 입력입니다. 다시 시도하세요.")
        selection = input(MENU_PROMPT)


menu()