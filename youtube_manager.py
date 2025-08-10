import json

def load_data():
    try:
        with open('youtube.txt','r') as file: 
            return json.load(file)
    except FileNotFoundError:
        return []
def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)

def list_all_videos(videos):
    print('\n')
    print('*' * 70)
    for index,video in  enumerate(videos,start=1):
        print(f"{index}. {video['name']}, duration : {video['time']}")

    print('\n')
    print('*' * 70)   
def add_videos(videos):
    name = input("Enter video name : ")
    time = input("Enter video time : ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_videos(videos):
    list_all_videos(videos)
    index= int(input("Enter the number video to be updated :"))
    if 1<=index <= len(videos):
        name=input("enter the new video name: ")
        time=input("enter the new video time: ")
        videos[index-1] = {'name':name,'time':time}
        save_data_helper(videos)
    else:
        print("invalid index selected")

def delete_videos(videos):
    list_all_videos(videos)
    index = int(input("Enter the number video to be deleted : "))
    if 1<=index <= len(videos):
       del videos[index-1]
       save_data_helper(videos)
    else:
        print("invalid index selected")

def main():
    videos = load_data()
    while True :
        print("\n Youtube Manager | choose an option")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video's details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")

        # print(videos)

        choice = input("Enter a choice : ")

        match choice:
            case '1' :
                list_all_videos(videos)
            case '2' :
                add_videos(videos)
            case '3':
                update_videos(videos)
            case '4':
                delete_videos(videos)
            case '5':
                break
            case  _:
                print("invalid choice")
if __name__ == "__main__":
    main()