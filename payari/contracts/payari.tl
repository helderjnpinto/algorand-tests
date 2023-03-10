#pragma version 7

if Txn.ApplicationID == 0:
    # Create app
    exit(1)
end

switch Txn.OnCompletion:
    NoOp: main
    OptIn: opt_in
    CloseOut: close_out
    UpdateApplication: update_app
    DeleteApplication: delete_app
end

block opt_in:
    # Disallow Opt In
    exit(0)
end

block close_out:
    # Disallow Closing Out
    exit(0)
end

block update_app:
    # Only allow the Creator to update the app
    exit(Txn.Sender == Global.CreatorAddress)
end

block delete_app:
    # Only allow the Creator to delete the app
    exit(Txn.Sender == Global.CreatorAddress)
end

block main:
    switch Txn.ApplicationArgs[0]:
        "add": add
    end

    block add:
        # some statements here
        int return_value = method_add()
        log(concat("add return value logx %i", itob(return_value)))
        exit(1)
    end

end


func method_add() int:
    int arg1 = btoi(Txn.ApplicationArgs[1])
    int arg2 = btoi(Txn.ApplicationArgs[2])
    return arg1 + arg2
end

