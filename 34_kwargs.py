""" kwargs """

# argumnet akan otomatis menjadi dictionary


def fungsi(**kwargs):
    """
    kwargs
    """
    print(kwargs.get("nama"))


fungsi(nama="Bagus")
