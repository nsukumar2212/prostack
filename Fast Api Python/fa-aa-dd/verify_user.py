from fastapi import HTTPException
def verify_user():
    user_name="Sonia"

    if user_name !="Rahul":
        raise HTTPException(status_code=404,detail="User not Authorize")

    return user_name