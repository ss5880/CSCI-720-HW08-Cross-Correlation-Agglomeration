class Cluster:
    def __init__(self, User_ID, x, y):
        self.User_ID = User_ID
        self.size = 1
        self.x = x
        self.y = y

    def __str__(self):
        return"(ID:%s x:%s y:%s)" % (self.User_ID, self.x, self.y)

    def __eq__(self, other):
        if not isinstance(other, Cluster):
            return NotImplemented
        return self.User_ID == other.User_ID


class Center_of_Mass:
    def __init__(self, COM_ID, Cluster_ID):
        self.COM_ID = COM_ID
        self.Cluster_ID = Cluster_ID

class Marged_Cluster:
    def __init__(self, num_COM_ID, cluster1, cluster2):
        self.num_COM_ID = num_COM_ID
        self.cluster1 = cluster1
        self.cluster2 = cluster2
        if cluster1.size == cluster2.size:
            self.size = cluster1.size + cluster2.size
        else:
            self.size = min(cluster1.size, cluster2.size)
        self.COM_x = None
        self.COM_y = None

    def get_com(c1_x, c1_y, c2_x, c2_y):
        COM_x = (c1_x + c2_x) / 2
        COM_y = (c1_y + c2_y) / 2
        return COM_x, COM_y

    def __eq__(self, other):
        if isinstance(other, Marged_Cluster):
            return self.num_COM_ID == other.num_COM_ID
        else:
            return False

    def __str__(self):
        return"[ID:%s c1:%s c2:%s size:%s]" % (self.num_COM_ID, self.cluster1, self.cluster2, self.size)
