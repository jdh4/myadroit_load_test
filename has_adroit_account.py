import os
import pandas as pd
import dossier

df = pd.read_csv("data.csv")
df.name.value_counts()

def dir_exists(netid):
    netids = [netid]
    yy = pd.DataFrame(dossier.ldap_plus(netids))
    headers = yy.iloc[0]
    yy = pd.DataFrame(yy.values[1:], columns=headers)
    netid_true = yy["NETID_TRUE"].values[0]
    print(netid, netid_true)
    return "No" if os.path.exists(f"/home/{netid_true}") else "Yes"

df["NeedsAccount"] = df.uid.apply(lambda x: dir_exists(x))
df = df.sort_values("uid")
df = df.reset_index(drop=True)
df.index += 1
df = df[["uid", "NeedsAccount", "name" ]]
df.columns = ["NetID", "NeedsAccount", "Name"]
print(df.to_string(index=True))
print(" ".join((list(df.NetID.values))))
