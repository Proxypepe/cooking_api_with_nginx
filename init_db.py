from src.models.recipe import Recipe
from mongoengine import connect, disconnect

if __name__ == '__main__':
    connect(host='mongodb://localhost:27017/cooking_recipe')
    Recipe(
        name="Slow Cooker Salisbury Steak",
        description="This Salisbury steak recipe comes together quickly and does not need a lot of time in the slow "
                    "cooker. It's a delicious way to add flavor to ground beef and the children love it! The gravy is "
                    "delightful served over mashed potatoes.",
        prepare="15 mins",
        cook="4 hrs",
        ingredients=[
            "2 pounds lean ground beef",
            "1/2 cup Italian seasoned bread crumbs",
            "1/4 cup milk", "1 (1 ounce) envelope dry onion soup mix",
            "1/4 cup all-purpose flour",
            "2 tablespoons vegetable oil",
            "2 (10.5 ounce) cans condensed cream of chicken soup",
            "3/4 cup water",
            "1 (1 ounce) packet dry au jus mix"
        ],
        steps=[
            "Combine ground beef, bread crumbs, milk, and onion soup mix together in a large bowl until well "
            "combined; shape into 8 patties.",
            "Heat oil in a large skillet over medium-high heat. Dredge patties in flour just to coat, and quickly "
            "brown on both sides in the hot skillet. Place browned patties into the slow cooker stacking alternately "
            "like a pyramid.",
            "Mix condensed soup, water, and au jus mix together in a medium bowl; pour over the beef patties. Cook on "
            "Low until ground beef is well done, about 4 to 5 hours.",
        ],
        file_name="slow_cooker_salisbury_steak.png",
        servings=8,
        tags=["Beef", "Fire", "Main Dishes"],
    ).save()

    Recipe(
        name="Beef Stroganoff",
        description="This is the best beef stroganoff recipe I know. It's well worth the effort. I have been making "
                    "this for over 20 years!",
        prepare="15 mins",
        cook="1 hr 15 mins",
        ingredients=[
            "2 pounds beef chuck roast",
            "1/2 teaspoon salt",
            "1/2 teaspoon ground black pepper",
            "4 ounces butter",
            "4 green onions, sliced (white parts only)",
            "4 tablespoons all-purpose flour",
            "1 (10.5 ounce) can condensed beef broth",
            "1 teaspoon prepared mustard",
            "1 (6 ounce) can sliced mushrooms, drained",
            "1/3 cup sour cream",
            "1/3 cup white wine",
            "salt and ground black pepper to taste",
        ],
        steps=[
            "Remove any fat and gristle from chuck roast; cut into strips 1/2-inch thick by 2-inches long. Season with 1/2 teaspoon salt and 1/2 teaspoon pepper.",
            "Melt butter in a large skillet over medium heat. Add beef and brown quickly; push to one side of the skillet. Add onions; cook and stir for 3 to 5 minutes, then push to the side with beef.",
            "Stir flour into juices on the empty side of the pan. Pour in beef broth and bring to a boil, stirring constantly. Lower the heat and stir in mustard. Cover and simmer for 1 hour or until the beef is tender.",
            "Five minutes before serving, stir in mushrooms, sour cream, and white wine. Cook until heated through; season to taste with salt and pepper.",
        ],
        file_name="beef_stroganoff.jpg",
        servings=8,
        tags=["Beef"],
    ).save()

    Recipe(
        name="Best Steak Marinade in Existence",
        description="This is a family recipe that has been developed only over the last 5 years. In this short time it's made me famous in our close circle, but until now I've never shared it with anyone.",
        prepare="15 mins",
        cook="1 hr",
        ingredients=[
            "1/3 cup soy sauce",
            "1/2 cup olive oil",
            "1/3 cup fresh lemon juice",
            "1/4 cup Worcestershire sauce",
            "1 1/2 tablespoons garlic powder",
            "3 tablespoons dried basil",
            "1 1/2 tablespoons dried parsley flakes",
            "1 teaspoon ground white pepper",
            "1/4 teaspoon hot pepper sauce (Optional)",
            "1 teaspoon dried minced garlic (Optional)",
        ],
        steps=[
            "Place the soy sauce, olive oil, lemon juice, Worcestershire sauce, garlic powder, basil, parsley, and pepper in a blender. Add hot pepper sauce and garlic, if desired. Blend on high speed for 30 seconds until thoroughly mixed.",
            "Pour marinade over desired type of meat. Cover, and refrigerate for up to 8 hours. Cook meat as desired."
        ],
        file_name="steak_marinade.jpg",
        servings=8,
        tags=["Beef"],
    ).save()

    disconnect()
