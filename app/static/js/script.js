const homeStates = {
    profile_active: false
};

const handleProfileClick = () => {

    //get menu element
    const profileMenuElement = document.getElementById('profile-menu')

    const exitingStates = [
        "transition",
        "ease-in",
        "duration-75",
        "transform",
        "opacity-0",
        "scale-95"
    ]

    const enteringStates = [
        "transition",
        "ease-out",
        "duration-100",
        "transform",
        "opacity-100",
        "scale-100"
    ]

    if (!homeStates.profile_active){

        profileMenuElement.classList.remove(...exitingStates)
        profileMenuElement.classList.add(...enteringStates)

        homeStates.profile_active = true

        return
    }

    profileMenuElement.classList.remove(...enteringStates)
    profileMenuElement.classList.add(...exitingStates)

    homeStates.profile_active = false
    
}


// add event listener
const userProfileButton = document.getElementById('user-menu-button')
userProfileButton.addEventListener('click', handleProfileClick)
