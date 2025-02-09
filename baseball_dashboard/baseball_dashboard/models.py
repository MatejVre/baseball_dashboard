# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class People(models.Model):
    id_custom = models.BigIntegerField(db_column='ID_custom', blank=True, null=True)  # Field name made lowercase.
    playerid = models.TextField(primary_key=True, db_column='playerID', blank=True)  # Field name made lowercase.
    birthyear = models.FloatField(db_column='birthYear', blank=True, null=True)  # Field name made lowercase.
    birthmonth = models.FloatField(db_column='birthMonth', blank=True, null=True)  # Field name made lowercase.
    birthday = models.FloatField(db_column='birthDay', blank=True, null=True)  # Field name made lowercase.
    birthcity = models.TextField(db_column='birthCity', blank=True, null=True)  # Field name made lowercase.
    birthcountry = models.TextField(db_column='birthCountry', blank=True, null=True)  # Field name made lowercase.
    birthstate = models.TextField(db_column='birthState', blank=True, null=True)  # Field name made lowercase.
    deathyear = models.FloatField(db_column='deathYear', blank=True, null=True)  # Field name made lowercase.
    deathmonth = models.FloatField(db_column='deathMonth', blank=True, null=True)  # Field name made lowercase.
    deathday = models.FloatField(db_column='deathDay', blank=True, null=True)  # Field name made lowercase.
    deathcountry = models.TextField(db_column='deathCountry', blank=True, null=True)  # Field name made lowercase.
    deathstate = models.TextField(db_column='deathState', blank=True, null=True)  # Field name made lowercase.
    deathcity = models.TextField(db_column='deathCity', blank=True, null=True)  # Field name made lowercase.
    namefirst = models.TextField(db_column='nameFirst', blank=True, null=True)  # Field name made lowercase.
    namelast = models.TextField(db_column='nameLast', blank=True, null=True)  # Field name made lowercase.
    namegiven = models.TextField(db_column='nameGiven', blank=True, null=True)  # Field name made lowercase.
    weight = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    bats = models.TextField(blank=True, null=True)
    throws = models.TextField(blank=True, null=True)
    debut = models.TextField(blank=True, null=True)
    bbrefid = models.TextField(db_column='bbrefID', blank=True, null=True)  # Field name made lowercase.
    finalgame = models.TextField(db_column='finalGame', blank=True, null=True)  # Field name made lowercase.
    retroid = models.TextField(db_column='retroID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'People'

class Teams(models.Model):
    pk = models.CompositePrimaryKey("yearid", "lgid", "teamid")
    yearid = models.BigIntegerField(db_column='yearID', blank=True)  # Field name made lowercase.
    lgid = models.TextField(db_column='lgID', blank=True)  # Field name made lowercase.
    teamid = models.TextField(db_column='teamID', blank=True)  # Field name made lowercase.
    franchid = models.TextField(db_column='franchID', blank=True, null=True)  # Field name made lowercase.
    divid = models.TextField(db_column='divID', blank=True, null=True)  # Field name made lowercase.
    rank = models.BigIntegerField(db_column='Rank', blank=True, null=True)  # Field name made lowercase.
    g = models.BigIntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    ghome = models.FloatField(db_column='Ghome', blank=True, null=True)  # Field name made lowercase.
    w = models.BigIntegerField(db_column='W', blank=True, null=True)  # Field name made lowercase.
    l = models.BigIntegerField(db_column='L', blank=True, null=True)  # Field name made lowercase.
    divwin = models.TextField(db_column='DivWin', blank=True, null=True)  # Field name made lowercase.
    wcwin = models.TextField(db_column='WCWin', blank=True, null=True)  # Field name made lowercase.
    lgwin = models.TextField(db_column='LgWin', blank=True, null=True)  # Field name made lowercase.
    wswin = models.TextField(db_column='WSWin', blank=True, null=True)  # Field name made lowercase.
    r = models.BigIntegerField(db_column='R', blank=True, null=True)  # Field name made lowercase.
    ab = models.BigIntegerField(db_column='AB', blank=True, null=True)  # Field name made lowercase.
    h = models.BigIntegerField(db_column='H', blank=True, null=True)  # Field name made lowercase.
    number_2b = models.BigIntegerField(db_column='2B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3b = models.BigIntegerField(db_column='3B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    hr = models.BigIntegerField(db_column='HR', blank=True, null=True)  # Field name made lowercase.
    bb = models.BigIntegerField(db_column='BB', blank=True, null=True)  # Field name made lowercase.
    so = models.FloatField(db_column='SO', blank=True, null=True)  # Field name made lowercase.
    sb = models.FloatField(db_column='SB', blank=True, null=True)  # Field name made lowercase.
    cs = models.FloatField(db_column='CS', blank=True, null=True)  # Field name made lowercase.
    hbp = models.FloatField(db_column='HBP', blank=True, null=True)  # Field name made lowercase.
    sf = models.FloatField(db_column='SF', blank=True, null=True)  # Field name made lowercase.
    ra = models.BigIntegerField(db_column='RA', blank=True, null=True)  # Field name made lowercase.
    er = models.BigIntegerField(db_column='ER', blank=True, null=True)  # Field name made lowercase.
    era = models.FloatField(db_column='ERA', blank=True, null=True)  # Field name made lowercase.
    cg = models.BigIntegerField(db_column='CG', blank=True, null=True)  # Field name made lowercase.
    sho = models.BigIntegerField(db_column='SHO', blank=True, null=True)  # Field name made lowercase.
    sv = models.BigIntegerField(db_column='SV', blank=True, null=True)  # Field name made lowercase.
    ipouts = models.BigIntegerField(db_column='IPouts', blank=True, null=True)  # Field name made lowercase.
    ha = models.BigIntegerField(db_column='HA', blank=True, null=True)  # Field name made lowercase.
    hra = models.BigIntegerField(db_column='HRA', blank=True, null=True)  # Field name made lowercase.
    bba = models.BigIntegerField(db_column='BBA', blank=True, null=True)  # Field name made lowercase.
    soa = models.BigIntegerField(db_column='SOA', blank=True, null=True)  # Field name made lowercase.
    e = models.BigIntegerField(db_column='E', blank=True, null=True)  # Field name made lowercase.
    dp = models.BigIntegerField(db_column='DP', blank=True, null=True)  # Field name made lowercase.
    fp = models.FloatField(db_column='FP', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(blank=True, null=True)
    park = models.TextField(blank=True, null=True)
    attendance = models.FloatField(blank=True, null=True)
    bpf = models.BigIntegerField(db_column='BPF', blank=True, null=True)  # Field name made lowercase.
    ppf = models.BigIntegerField(db_column='PPF', blank=True, null=True)  # Field name made lowercase.
    teamidbr = models.TextField(db_column='teamIDBR', blank=True, null=True)  # Field name made lowercase.
    teamidlahman45 = models.TextField(db_column='teamIDlahman45', blank=True, null=True)  # Field name made lowercase.
    teamidretro = models.TextField(db_column='teamIDretro', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Teams'

class Allstarfull(models.Model):
    playerid = models.ForeignKey(People, db_column='playerID', blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.
    yearid = models.BigIntegerField(db_column='yearID', blank=True, null=True)  # Field name made lowercase.
    gamenum = models.BigIntegerField(db_column='gameNum', blank=True, null=True)  # Field name made lowercase.
    gameid = models.TextField(db_column='gameID', blank=True, null=True)  # Field name made lowercase.
    teamid = models.TextField(db_column='teamID', blank=True, null=True)  # Field name made lowercase.
    lgid = models.TextField(db_column='lgID', blank=True, null=True)  # Field name made lowercase.
    gp = models.BigIntegerField(db_column='GP', blank=True, null=True)  # Field name made lowercase.
    startingpos = models.FloatField(db_column='startingPos', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'AllstarFull'


class Appearances(models.Model):
    pk = models.CompositePrimaryKey("yearid", "teamid")
    yearid = models.BigIntegerField(db_column='yearID', blank=True)  # Field name made lowercase.
    teamid = models.TextField(db_column='teamID', blank=True)  # Field name made lowercase.
    lgid = models.TextField(db_column='lgID', blank=True, null=True)  # Field name made lowercase.
    playerid = models.ForeignKey(People, db_column='playerID', blank=True, null=True, on_delete=models.CASCADE)
    g_all = models.BigIntegerField(db_column='G_all', blank=True, null=True)  # Field name made lowercase.
    gs = models.FloatField(db_column='GS', blank=True, null=True)  # Field name made lowercase.
    g_batting = models.BigIntegerField(db_column='G_batting', blank=True, null=True)  # Field name made lowercase.
    g_defense = models.FloatField(db_column='G_defense', blank=True, null=True)  # Field name made lowercase.
    g_p = models.BigIntegerField(db_column='G_p', blank=True, null=True)  # Field name made lowercase.
    g_c = models.BigIntegerField(db_column='G_c', blank=True, null=True)  # Field name made lowercase.
    g_1b = models.BigIntegerField(db_column='G_1b', blank=True, null=True)  # Field name made lowercase.
    g_2b = models.BigIntegerField(db_column='G_2b', blank=True, null=True)  # Field name made lowercase.
    g_3b = models.BigIntegerField(db_column='G_3b', blank=True, null=True)  # Field name made lowercase.
    g_ss = models.BigIntegerField(db_column='G_ss', blank=True, null=True)  # Field name made lowercase.
    g_lf = models.BigIntegerField(db_column='G_lf', blank=True, null=True)  # Field name made lowercase.
    g_cf = models.BigIntegerField(db_column='G_cf', blank=True, null=True)  # Field name made lowercase.
    g_rf = models.BigIntegerField(db_column='G_rf', blank=True, null=True)  # Field name made lowercase.
    g_of = models.BigIntegerField(db_column='G_of', blank=True, null=True)  # Field name made lowercase.
    g_dh = models.FloatField(db_column='G_dh', blank=True, null=True)  # Field name made lowercase.
    g_ph = models.FloatField(db_column='G_ph', blank=True, null=True)  # Field name made lowercase.
    g_pr = models.FloatField(db_column='G_pr', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Appearances'


class Awardsmanagers(models.Model):
    playerid = models.ForeignKey(People, db_column='playerID', blank=True, null=True, on_delete=models.CASCADE)
    awardid = models.TextField(db_column='awardID', blank=True, null=True)  # Field name made lowercase.
    yearid = models.BigIntegerField(db_column='yearID', blank=True, null=True)  # Field name made lowercase.
    lgid = models.TextField(db_column='lgID', blank=True, null=True)  # Field name made lowercase.
    tie = models.TextField(blank=True, null=True)
    notes = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'AwardsManagers'


class Awardsplayers(models.Model):
    playerid = models.ForeignKey(People, db_column='playerID', blank=True, null=True, on_delete=models.CASCADE)
    awardid = models.TextField(db_column='awardID', blank=True, null=True)  # Field name made lowercase.
    yearid = models.BigIntegerField(db_column='yearID', blank=True, null=True)  # Field name made lowercase.
    lgid = models.TextField(db_column='lgID', blank=True, null=True)  # Field name made lowercase.
    tie = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'AwardsPlayers'


class Awardssharemanagers(models.Model):
    awardid = models.TextField(db_column='awardID', blank=True, null=True)  # Field name made lowercase.
    yearid = models.BigIntegerField(db_column='yearID', blank=True, null=True)  # Field name made lowercase.
    lgid = models.TextField(db_column='lgID', blank=True, null=True)  # Field name made lowercase.
    playerid = models.ForeignKey(People, db_column='playerID', blank=True, null=True, on_delete=models.CASCADE)
    pointswon = models.BigIntegerField(db_column='pointsWon', blank=True, null=True)  # Field name made lowercase.
    pointsmax = models.FloatField(db_column='pointsMax', blank=True, null=True)  # Field name made lowercase.
    votesfirst = models.BigIntegerField(db_column='votesFirst', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'AwardsShareManagers'


class Awardsshareplayers(models.Model):
    awardid = models.TextField(db_column='awardID', blank=True, null=True)  # Field name made lowercase.
    yearid = models.BigIntegerField(db_column='yearID', blank=True, null=True)  # Field name made lowercase.
    lgid = models.TextField(db_column='lgID', blank=True, null=True)  # Field name made lowercase.
    playerid = models.ForeignKey(People, db_column='playerID', blank=True, null=True, on_delete=models.CASCADE)
    pointswon = models.BigIntegerField(db_column='pointsWon', blank=True, null=True)  # Field name made lowercase.
    pointsmax = models.BigIntegerField(db_column='pointsMax', blank=True, null=True)  # Field name made lowercase.
    votesfirst = models.FloatField(db_column='votesFirst', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'AwardsSharePlayers'


class Batting(models.Model):
    pk = models.CompositePrimaryKey("playerid", "yearid", "stint")
    playerid = models.ForeignKey(People, db_column='playerID', blank=True, on_delete=models.CASCADE)
    yearid = models.BigIntegerField(db_column='yearID', blank=True)  # Field name made lowercase.
    stint = models.BigIntegerField(blank=True)
    teamid = models.TextField(db_column='teamID', blank=True, null=True)  # Field name made lowercase.
    lgid = models.TextField(db_column='lgID', blank=True, null=True)  # Field name made lowercase.
    g = models.BigIntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    g_batting = models.FloatField(db_column='G_batting', blank=True, null=True)  # Field name made lowercase.
    ab = models.BigIntegerField(db_column='AB', blank=True, null=True)  # Field name made lowercase.
    r = models.BigIntegerField(db_column='R', blank=True, null=True)  # Field name made lowercase.
    h = models.BigIntegerField(db_column='H', blank=True, null=True)  # Field name made lowercase.
    number_2b = models.BigIntegerField(db_column='2B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3b = models.BigIntegerField(db_column='3B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    hr = models.BigIntegerField(db_column='HR', blank=True, null=True)  # Field name made lowercase.
    rbi = models.FloatField(db_column='RBI', blank=True, null=True)  # Field name made lowercase.
    sb = models.FloatField(db_column='SB', blank=True, null=True)  # Field name made lowercase.
    cs = models.FloatField(db_column='CS', blank=True, null=True)  # Field name made lowercase.
    bb = models.BigIntegerField(db_column='BB', blank=True, null=True)  # Field name made lowercase.
    so = models.FloatField(db_column='SO', blank=True, null=True)  # Field name made lowercase.
    ibb = models.FloatField(db_column='IBB', blank=True, null=True)  # Field name made lowercase.
    hbp = models.FloatField(db_column='HBP', blank=True, null=True)  # Field name made lowercase.
    sh = models.FloatField(db_column='SH', blank=True, null=True)  # Field name made lowercase.
    sf = models.FloatField(db_column='SF', blank=True, null=True)  # Field name made lowercase.
    gidp = models.FloatField(db_column='GIDP', blank=True, null=True)  # Field name made lowercase.
    g_old = models.FloatField(db_column='G_old', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Batting'


class Battingpost(models.Model):
    yearid = models.BigIntegerField(db_column='yearID', blank=True, null=True)  # Field name made lowercase.
    round = models.TextField(blank=True, null=True)
    playerid = models.ForeignKey(People, db_column='playerID', blank=True, null=True, on_delete=models.CASCADE)
    teamid = models.TextField(db_column='teamID', blank=True, null=True)  # Field name made lowercase.
    lgid = models.TextField(db_column='lgID', blank=True, null=True)  # Field name made lowercase.
    g = models.BigIntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    ab = models.BigIntegerField(db_column='AB', blank=True, null=True)  # Field name made lowercase.
    r = models.BigIntegerField(db_column='R', blank=True, null=True)  # Field name made lowercase.
    h = models.BigIntegerField(db_column='H', blank=True, null=True)  # Field name made lowercase.
    number_2b = models.BigIntegerField(db_column='2B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3b = models.BigIntegerField(db_column='3B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    hr = models.BigIntegerField(db_column='HR', blank=True, null=True)  # Field name made lowercase.
    rbi = models.BigIntegerField(db_column='RBI', blank=True, null=True)  # Field name made lowercase.
    sb = models.BigIntegerField(db_column='SB', blank=True, null=True)  # Field name made lowercase.
    cs = models.FloatField(db_column='CS', blank=True, null=True)  # Field name made lowercase.
    bb = models.BigIntegerField(db_column='BB', blank=True, null=True)  # Field name made lowercase.
    so = models.BigIntegerField(db_column='SO', blank=True, null=True)  # Field name made lowercase.
    ibb = models.BigIntegerField(db_column='IBB', blank=True, null=True)  # Field name made lowercase.
    hbp = models.FloatField(db_column='HBP', blank=True, null=True)  # Field name made lowercase.
    sh = models.FloatField(db_column='SH', blank=True, null=True)  # Field name made lowercase.
    sf = models.FloatField(db_column='SF', blank=True, null=True)  # Field name made lowercase.
    gidp = models.FloatField(db_column='GIDP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'BattingPost'


class Collegeplaying(models.Model):
    playerid = models.ForeignKey(People, db_column='playerID', blank=True, null=True, on_delete=models.CASCADE)
    schoolid = models.TextField(db_column='schoolID', blank=True, null=True)  # Field name made lowercase.
    yearid = models.BigIntegerField(db_column='yearID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'CollegePlaying'


class Fielding(models.Model):
    playerid = models.ForeignKey(People, db_column='playerID', blank=True, null=True, on_delete=models.CASCADE)
    yearid = models.BigIntegerField(db_column='yearID', blank=True, null=True)  # Field name made lowercase.
    stint = models.BigIntegerField(blank=True, null=True)
    teamid = models.TextField(db_column='teamID', blank=True, null=True)  # Field name made lowercase.
    lgid = models.TextField(db_column='lgID', blank=True, null=True)  # Field name made lowercase.
    pos = models.TextField(db_column='POS', blank=True, null=True)  # Field name made lowercase.
    g = models.BigIntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    gs = models.FloatField(db_column='GS', blank=True, null=True)  # Field name made lowercase.
    innouts = models.FloatField(db_column='InnOuts', blank=True, null=True)  # Field name made lowercase.
    po = models.BigIntegerField(db_column='PO', blank=True, null=True)  # Field name made lowercase.
    a = models.BigIntegerField(db_column='A', blank=True, null=True)  # Field name made lowercase.
    e = models.FloatField(db_column='E', blank=True, null=True)  # Field name made lowercase.
    dp = models.BigIntegerField(db_column='DP', blank=True, null=True)  # Field name made lowercase.
    pb = models.FloatField(db_column='PB', blank=True, null=True)  # Field name made lowercase.
    wp = models.FloatField(db_column='WP', blank=True, null=True)  # Field name made lowercase.
    sb = models.FloatField(db_column='SB', blank=True, null=True)  # Field name made lowercase.
    cs = models.FloatField(db_column='CS', blank=True, null=True)  # Field name made lowercase.
    zr = models.FloatField(db_column='ZR', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Fielding'


class Fieldingof(models.Model):
    playerid = models.ForeignKey(People, db_column='playerID', blank=True, null=True, on_delete=models.CASCADE)
    yearid = models.BigIntegerField(db_column='yearID', blank=True, null=True)  # Field name made lowercase.
    stint = models.BigIntegerField(blank=True, null=True)
    glf = models.FloatField(db_column='Glf', blank=True, null=True)  # Field name made lowercase.
    gcf = models.FloatField(db_column='Gcf', blank=True, null=True)  # Field name made lowercase.
    grf = models.FloatField(db_column='Grf', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'FieldingOF'


class Fieldingofsplit(models.Model):
    playerid = models.ForeignKey(People, db_column='playerID', blank=True, null=True, on_delete=models.CASCADE)
    yearid = models.BigIntegerField(db_column='yearID', blank=True, null=True)  # Field name made lowercase.
    stint = models.BigIntegerField(blank=True, null=True)
    teamid = models.TextField(db_column='teamID', blank=True, null=True)  # Field name made lowercase.
    lgid = models.TextField(db_column='lgID', blank=True, null=True)  # Field name made lowercase.
    pos = models.TextField(db_column='POS', blank=True, null=True)  # Field name made lowercase.
    g = models.BigIntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    gs = models.BigIntegerField(db_column='GS', blank=True, null=True)  # Field name made lowercase.
    innouts = models.BigIntegerField(db_column='InnOuts', blank=True, null=True)  # Field name made lowercase.
    po = models.BigIntegerField(db_column='PO', blank=True, null=True)  # Field name made lowercase.
    a = models.BigIntegerField(db_column='A', blank=True, null=True)  # Field name made lowercase.
    e = models.BigIntegerField(db_column='E', blank=True, null=True)  # Field name made lowercase.
    dp = models.BigIntegerField(db_column='DP', blank=True, null=True)  # Field name made lowercase.
    pb = models.FloatField(db_column='PB', blank=True, null=True)  # Field name made lowercase.
    wp = models.FloatField(db_column='WP', blank=True, null=True)  # Field name made lowercase.
    sb = models.FloatField(db_column='SB', blank=True, null=True)  # Field name made lowercase.
    cs = models.FloatField(db_column='CS', blank=True, null=True)  # Field name made lowercase.
    zr = models.FloatField(db_column='ZR', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'FieldingOFsplit'


class Fieldingpost(models.Model):
    playerid = models.ForeignKey(People, db_column='playerID', blank=True, null=True, on_delete=models.CASCADE)
    yearid = models.BigIntegerField(db_column='yearID', blank=True, null=True)  # Field name made lowercase.
    teamid = models.TextField(db_column='teamID', blank=True, null=True)  # Field name made lowercase.
    lgid = models.TextField(db_column='lgID', blank=True, null=True)  # Field name made lowercase.
    round = models.TextField(blank=True, null=True)
    pos = models.TextField(db_column='POS', blank=True, null=True)  # Field name made lowercase.
    g = models.BigIntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    gs = models.BigIntegerField(db_column='GS', blank=True, null=True)  # Field name made lowercase.
    innouts = models.BigIntegerField(db_column='InnOuts', blank=True, null=True)  # Field name made lowercase.
    po = models.BigIntegerField(db_column='PO', blank=True, null=True)  # Field name made lowercase.
    a = models.BigIntegerField(db_column='A', blank=True, null=True)  # Field name made lowercase.
    e = models.BigIntegerField(db_column='E', blank=True, null=True)  # Field name made lowercase.
    dp = models.BigIntegerField(db_column='DP', blank=True, null=True)  # Field name made lowercase.
    tp = models.BigIntegerField(db_column='TP', blank=True, null=True)  # Field name made lowercase.
    pb = models.FloatField(db_column='PB', blank=True, null=True)  # Field name made lowercase.
    sb = models.FloatField(db_column='SB', blank=True, null=True)  # Field name made lowercase.
    cs = models.FloatField(db_column='CS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'FieldingPost'


class Halloffame(models.Model):
    playerid = models.ForeignKey(People, db_column='playerID', blank=True, null=True, on_delete=models.CASCADE)
    yearid = models.BigIntegerField(blank=True, null=True)
    votedby = models.TextField(db_column='votedBy', blank=True, null=True)  # Field name made lowercase.
    ballots = models.FloatField(blank=True, null=True)
    needed = models.FloatField(blank=True, null=True)
    votes = models.FloatField(blank=True, null=True)
    inducted = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    needed_note = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'HallOfFame'


class Homegames(models.Model):
    yearkey = models.BigIntegerField(blank=True, null=True)
    leaguekey = models.TextField(blank=True, null=True)
    teamkey = models.TextField(blank=True, null=True)
    parkkey = models.TextField(blank=True, null=True)
    spanfirst = models.TextField(blank=True, null=True)
    spanlast = models.TextField(blank=True, null=True)
    games = models.BigIntegerField(blank=True, null=True)
    openings = models.BigIntegerField(blank=True, null=True)
    attendance = models.BigIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'HomeGames'


class Managers(models.Model):
    playerid = models.ForeignKey(People, db_column='playerID', blank=True, null=True, on_delete=models.CASCADE)
    yearid = models.BigIntegerField(db_column='yearID', blank=True, null=True)  # Field name made lowercase.
    teamid = models.TextField(db_column='teamID', blank=True, null=True)  # Field name made lowercase.
    lgid = models.TextField(db_column='lgID', blank=True, null=True)  # Field name made lowercase.
    inseason = models.BigIntegerField(blank=True, null=True)
    g = models.BigIntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    w = models.BigIntegerField(db_column='W', blank=True, null=True)  # Field name made lowercase.
    l = models.BigIntegerField(db_column='L', blank=True, null=True)  # Field name made lowercase.
    rank = models.BigIntegerField(blank=True, null=True)
    plyrmgr = models.TextField(db_column='plyrMgr', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Managers'


class Managershalf(models.Model):
    playerid = models.ForeignKey(People, db_column='playerID', blank=True, null=True, on_delete=models.CASCADE)
    yearid = models.BigIntegerField(db_column='yearID', blank=True, null=True)  # Field name made lowercase.
    teamid = models.TextField(db_column='teamID', blank=True, null=True)  # Field name made lowercase.
    lgid = models.TextField(db_column='lgID', blank=True, null=True)  # Field name made lowercase.
    inseason = models.BigIntegerField(blank=True, null=True)
    half = models.BigIntegerField(blank=True, null=True)
    g = models.BigIntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    w = models.BigIntegerField(db_column='W', blank=True, null=True)  # Field name made lowercase.
    l = models.BigIntegerField(db_column='L', blank=True, null=True)  # Field name made lowercase.
    rank = models.BigIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'ManagersHalf'


class Parks(models.Model):
    id = models.BigIntegerField(db_column='ID', blank=True, primary_key=True)  # Field name made lowercase.
    parkalias = models.TextField(blank=True, null=True)
    parkkey = models.TextField(blank=True, null=True)
    parkname = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'Parks'



class Pitching(models.Model):
    playerid = models.ForeignKey(People, db_column='playerID', blank=True, null=True, on_delete=models.CASCADE)
    yearid = models.BigIntegerField(db_column='yearID', blank=True, null=True)  # Field name made lowercase.
    stint = models.BigIntegerField(blank=True, null=True)
    teamid = models.TextField(db_column='teamID', blank=True, null=True)  # Field name made lowercase.
    lgid = models.TextField(db_column='lgID', blank=True, null=True)  # Field name made lowercase.
    w = models.BigIntegerField(db_column='W', blank=True, null=True)  # Field name made lowercase.
    l = models.BigIntegerField(db_column='L', blank=True, null=True)  # Field name made lowercase.
    g = models.BigIntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    gs = models.BigIntegerField(db_column='GS', blank=True, null=True)  # Field name made lowercase.
    cg = models.BigIntegerField(db_column='CG', blank=True, null=True)  # Field name made lowercase.
    sho = models.BigIntegerField(db_column='SHO', blank=True, null=True)  # Field name made lowercase.
    sv = models.BigIntegerField(db_column='SV', blank=True, null=True)  # Field name made lowercase.
    ipouts = models.BigIntegerField(db_column='IPouts', blank=True, null=True)  # Field name made lowercase.
    h = models.BigIntegerField(db_column='H', blank=True, null=True)  # Field name made lowercase.
    er = models.BigIntegerField(db_column='ER', blank=True, null=True)  # Field name made lowercase.
    hr = models.BigIntegerField(db_column='HR', blank=True, null=True)  # Field name made lowercase.
    bb = models.BigIntegerField(db_column='BB', blank=True, null=True)  # Field name made lowercase.
    so = models.BigIntegerField(db_column='SO', blank=True, null=True)  # Field name made lowercase.
    baopp = models.FloatField(db_column='BAOpp', blank=True, null=True)  # Field name made lowercase.
    era = models.FloatField(db_column='ERA', blank=True, null=True)  # Field name made lowercase.
    ibb = models.FloatField(db_column='IBB', blank=True, null=True)  # Field name made lowercase.
    wp = models.BigIntegerField(db_column='WP', blank=True, null=True)  # Field name made lowercase.
    hbp = models.FloatField(db_column='HBP', blank=True, null=True)  # Field name made lowercase.
    bk = models.BigIntegerField(db_column='BK', blank=True, null=True)  # Field name made lowercase.
    bfp = models.FloatField(db_column='BFP', blank=True, null=True)  # Field name made lowercase.
    gf = models.BigIntegerField(db_column='GF', blank=True, null=True)  # Field name made lowercase.
    r = models.BigIntegerField(db_column='R', blank=True, null=True)  # Field name made lowercase.
    sh = models.FloatField(db_column='SH', blank=True, null=True)  # Field name made lowercase.
    sf = models.FloatField(db_column='SF', blank=True, null=True)  # Field name made lowercase.
    gidp = models.FloatField(db_column='GIDP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Pitching'


class Pitchingpost(models.Model):
    playerid = models.ForeignKey(People, db_column='playerID', blank=True, null=True, on_delete=models.CASCADE)
    yearid = models.BigIntegerField(db_column='yearID', blank=True, null=True)  # Field name made lowercase.
    round = models.TextField(blank=True, null=True)
    teamid = models.TextField(db_column='teamID', blank=True, null=True)  # Field name made lowercase.
    lgid = models.TextField(db_column='lgID', blank=True, null=True)  # Field name made lowercase.
    w = models.BigIntegerField(db_column='W', blank=True, null=True)  # Field name made lowercase.
    l = models.BigIntegerField(db_column='L', blank=True, null=True)  # Field name made lowercase.
    g = models.BigIntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    gs = models.BigIntegerField(db_column='GS', blank=True, null=True)  # Field name made lowercase.
    cg = models.BigIntegerField(db_column='CG', blank=True, null=True)  # Field name made lowercase.
    sho = models.BigIntegerField(db_column='SHO', blank=True, null=True)  # Field name made lowercase.
    sv = models.BigIntegerField(db_column='SV', blank=True, null=True)  # Field name made lowercase.
    ipouts = models.BigIntegerField(db_column='IPouts', blank=True, null=True)  # Field name made lowercase.
    h = models.BigIntegerField(db_column='H', blank=True, null=True)  # Field name made lowercase.
    er = models.BigIntegerField(db_column='ER', blank=True, null=True)  # Field name made lowercase.
    hr = models.BigIntegerField(db_column='HR', blank=True, null=True)  # Field name made lowercase.
    bb = models.BigIntegerField(db_column='BB', blank=True, null=True)  # Field name made lowercase.
    so = models.BigIntegerField(db_column='SO', blank=True, null=True)  # Field name made lowercase.
    baopp = models.FloatField(db_column='BAOpp', blank=True, null=True)  # Field name made lowercase.
    era = models.FloatField(db_column='ERA', blank=True, null=True)  # Field name made lowercase.
    ibb = models.FloatField(db_column='IBB', blank=True, null=True)  # Field name made lowercase.
    wp = models.FloatField(db_column='WP', blank=True, null=True)  # Field name made lowercase.
    hbp = models.FloatField(db_column='HBP', blank=True, null=True)  # Field name made lowercase.
    bk = models.FloatField(db_column='BK', blank=True, null=True)  # Field name made lowercase.
    bfp = models.FloatField(db_column='BFP', blank=True, null=True)  # Field name made lowercase.
    gf = models.BigIntegerField(db_column='GF', blank=True, null=True)  # Field name made lowercase.
    r = models.BigIntegerField(db_column='R', blank=True, null=True)  # Field name made lowercase.
    sh = models.FloatField(db_column='SH', blank=True, null=True)  # Field name made lowercase.
    sf = models.FloatField(db_column='SF', blank=True, null=True)  # Field name made lowercase.
    gidp = models.FloatField(db_column='GIDP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'PitchingPost'


class Salaries(models.Model):
    yearid = models.BigIntegerField(db_column='yearID', blank=True, null=True)  # Field name made lowercase.
    teamid = models.TextField(db_column='teamID', blank=True, null=True)  # Field name made lowercase.
    lgid = models.TextField(db_column='lgID', blank=True, null=True)  # Field name made lowercase.
    playerid = models.ForeignKey(People, db_column='playerID', blank=True, null=True, on_delete=models.CASCADE)
    salary = models.BigIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'Salaries'


class Seriespost(models.Model):
    yearid = models.BigIntegerField(db_column='yearID', blank=True, null=True)  # Field name made lowercase.
    round = models.TextField(blank=True, null=True)
    teamidwinner = models.TextField(db_column='teamIDwinner', blank=True, null=True)  # Field name made lowercase.
    lgidwinner = models.TextField(db_column='lgIDwinner', blank=True, null=True)  # Field name made lowercase.
    teamidloser = models.TextField(db_column='teamIDloser', blank=True, null=True)  # Field name made lowercase.
    lgidloser = models.TextField(db_column='lgIDloser', blank=True, null=True)  # Field name made lowercase.
    wins = models.BigIntegerField(blank=True, null=True)
    losses = models.BigIntegerField(blank=True, null=True)
    ties = models.BigIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'SeriesPost'





class Teamsfranchises(models.Model):
    franchid = models.TextField(db_column='franchID', blank=True, null=True)  # Field name made lowercase.
    franchname = models.TextField(db_column='franchName', blank=True, null=True)  # Field name made lowercase.
    active = models.TextField(blank=True, null=True)
    naassoc = models.TextField(db_column='NAassoc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'TeamsFranchises'


class Teamshalf(models.Model):
    yearid = models.BigIntegerField(db_column='yearID', blank=True, null=True)  # Field name made lowercase.
    lgid = models.TextField(db_column='lgID', blank=True, null=True)  # Field name made lowercase.
    teamid = models.TextField(db_column='teamID', blank=True, null=True)  # Field name made lowercase.
    half = models.BigIntegerField(db_column='Half', blank=True, null=True)  # Field name made lowercase.
    divid = models.TextField(db_column='divID', blank=True, null=True)  # Field name made lowercase.
    divwin = models.TextField(db_column='DivWin', blank=True, null=True)  # Field name made lowercase.
    rank = models.BigIntegerField(db_column='Rank', blank=True, null=True)  # Field name made lowercase.
    g = models.BigIntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    w = models.BigIntegerField(db_column='W', blank=True, null=True)  # Field name made lowercase.
    l = models.BigIntegerField(db_column='L', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'TeamsHalf'

