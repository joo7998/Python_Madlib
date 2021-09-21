# Kylie Ying (freeCodeCamp.org)

# string concatenation : "subscribe to ___"

youtuber = "Madfit"

print("subscribe to " + youtuber)
print("subscribe to {}".format(youtuber))
print(f"subscribe to {youtuber}")

adj = input("Adjective: ")
verb = input("Verb: ")
famous_person = input("Famous Person: ")

madlib = f"Computer programming is so {adj}! And I love to {verb}. I feel like {famous_person}."

print(madlib)