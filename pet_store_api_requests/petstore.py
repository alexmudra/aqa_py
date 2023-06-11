import requests

class Petstore():
    base_url = "https://petstore.swagger.io/v2"
    pet_status_codes = ["pending", "available", "sold"]
    pet_path = "/pet/"
    pet_findstatus_path_param = "/pet/findByStatus"

    headers = {
        'Content-Type': 'application/json',
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
    }

    def print_server_response(self, r):
        '''Print response information'''
        print("<---")
        print("Server status response:", r.status_code)
        print("Server response in json format:", r.json())
        print("--->")


    # def check_pet_id_in_endpoints(self, pet_id: str) -> None:
    #     print(self.base_url + self.pet_findstatus_path_param + self.pet_status_codes[0])
    #     # endpoints = [
    #     #     "https://petstore.swagger.io/v2/pet/findByStatus?status=pending",
    #     #     "https://petstore.swagger.io/v2/pet/findByStatus?status=available",
    #     #     "https://petstore.swagger.io/v2/pet/findByStatus?status=sold"
    #     # ]
    #
    #     endpoints = [
    #         self.base_url + self.pet_findstatus_path_param + "?status=" + self.pet_status_codes[0],
    #         self.base_url + self.pet_findstatus_path_param + "?status=" + self.pet_status_codes[1],
    #         self.base_url + self.pet_findstatus_path_param + "?status=" + self.pet_status_codes[2]
    #     ]
    #
    #     for endpoint in endpoints:
    #         try:
    #             response = requests.get(endpoint)
    #             response.raise_for_status()  # Генеруєм виняток, якщо статус відповіді не є 200 (OK)
    #             response_json_pets = response.json()
    #             # print("json respoonse iz pets", response_json_pets)
    #             for pet in response_json_pets:
    #                 if pet["id"] == pet_id:
    #                     print("Pet Found:")
    #                     print("ID:", pet["id"])
    #                     print("Name:", pet["name"])
    #                     print("Status:", pet["status"])
    #                     return response_json_pets
    #         except requests.exceptions.RequestException as e:
    #             print("Error occurred during request:", str(e))
    #
    #     print("Pet not found.")

    def check_pet_id_in_endpoints(self, pet_id: str) -> None:
        endpoints = [
            self.base_url + "/pet/findByStatus?status=" + self.pet_status_codes[0],
            self.base_url + "/pet/findByStatus?status=" + self.pet_status_codes[1],
            self.base_url + "/pet/findByStatus?status=" + self.pet_status_codes[2]
        ]

        for endpoint in endpoints:
            try:
                response = requests.get(endpoint)
                response.raise_for_status()
                response_json_pets = response.json()
                for pet in response_json_pets:
                    if pet["id"] == pet_id:
                        print("Pet Found:")
                        print("ID:", pet["id"])
                        print("Name:", pet["name"])
                        print("Status:", pet["status"])
                        return response_json_pets
            except requests.exceptions.RequestException as e:
                print("Error occurred during request:", str(e))

        print("Pet not found.")


    def get_petstore_status(self):
        '''Get pets status in petstore'''
        pet_findstatus_path_param = "/pet/findByStatus"
        headers = {
            'Content-Type': 'application/json',
            'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
        }

        user_prompt = input("To get pets status, print: pending, available, or sold: ")
        try:
            if user_prompt not in self.pet_status_codes:
                raise ValueError(f"Your input is:<{user_prompt}>, doesn't match {self.pet_status_codes}. Try again")

            params = {"status": user_prompt}
            url = self.base_url + pet_findstatus_path_param

            r = requests.get(url, headers=headers, params=params)
            self.print_server_response(r)
        except ValueError as e:
            print(e)


    def add_pet_to_store(self, name:str, status:str):
        '''Додати нову тварину (метод POST).
        Створіть новий об'єкт тварини з необхідною інформацією, наприклад, ім'я та статус.
        Зробіть запит до /pet з об'єктом тварини в тілі запиту, щоб додати нову тварину.
        Обробіть відповідь сервера та виведіть підтвердження про додавання тварини на екран.'''

        pet_create_path_param = "/pet"
        headers = {
            'Content-Type': 'application/json',
            'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
        }
        data = {
                "id": 0,
                "category": {
                    "id": 0,
                    "name": "string"
                },
                "name": name,
                "photoUrls": [
                    "string"
                ],
                "tags": [
                    {
                        "id": 0,
                        "name": "string"
                    }
                ],
                "status": status
        }
        try:
            if len(name)== 0 or len(status)== 0:
                raise ValueError(f"Your send empty parametr:name<{name}> or status<{status}>. Empty str name or status are prohibited. Try again!")
            if status not in self.pet_status_codes:
                raise ValueError(f"You send invalid paramet:status<{status}>. Remainder! Valid status list:{self.pet_status_codes}. Try again")
            url = self.base_url + pet_create_path_param
            r = requests.post(url, headers=headers, json=data)
            self.print_server_response(r)
            json_response = r.json()
            pet_name = json_response["name"]
            pet_status = json_response["status"]
            pet_id = json_response["id"]
            print(f"Response name is <{pet_name}> and status is <{pet_status}>")
            # print(f"Response id<{pet_id}>")

        except ValueError as e:
            print(e)


    def find_pet_by_id(self, pet_id:str):
        '''Знайти тварину за ідентифікатором (метод GET).
        Введіть ідентифікатор тварини, яку потрібно знайти.
        Зробіть запит до /pet/{petId}, де {petId} - ідентифікатор шуканої тварини.
        Обробіть відповідь сервера та виведіть інформацію про знайдену тварину на екран.'''
        pet_path = "/pet/"
        headers = {
            'Content-Type': 'application/json',
            'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
        }

        user_prompt = input("To get information about PET, input PET_ID: ")
        url = self.base_url + pet_path + user_prompt
        r = requests.get(url, headers=headers)
        self.print_server_response(r)


    def delete_pet_by_id(self, pet_id: str):
        '''Видалити тварину за ідентифікатором (метод DELETE).
        Введіть ідентифікатор тварини, яку потрібно видалити.
        Зробіть запит до /pet/{petId}, де {petId} - ідентифікатор тварини, яку потрібно видалити.
        Обробіть відповідь.'''

        try:
            url = self.base_url + self.pet_path + pet_id
            r = requests.delete(url, headers=self.headers)
            if r.status_code == 200:
                print(
                    f"Congratulations, you have successfully deleted information about pet <{pet_id}> from our system!")
            elif r.status_code == 400:
                raise ValueError("Invalid PET_ID. Please try again.")
            elif r.status_code == 404:
                raise ValueError("Pet not found. Please try again.")
            else:
                raise ValueError("An error occurred while deleting the pet.")
        except ValueError as e:
            print(e)





#9223372036854630556
#9223372036854632710
#9223372036854632716

#9223372036854633614
#9223372036854633617
#9223372036854633618

if __name__ == "__main__":
    petstore = Petstore()
    # petstore.get_petstore_status()
    # petstore.add_pet_to_store("t", "pending")
    # petstore.find_pet_by_id("9223372036854632710")
    # petstore.check_pet_id_in_endpoints("9223372036854632716")
    petstore.delete_pet_by_id("9223372036854633618")
