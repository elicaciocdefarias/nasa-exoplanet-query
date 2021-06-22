from django.db import models


class Exoplanet(models.Model):
    pl_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    hostname = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    #
    default_flag = models.IntegerField(
        null=True,
        blank=True,
    )
    sy_snum = models.IntegerField(
        null=True,
        blank=True,
    )
    sy_pnum = models.IntegerField(
        null=True,
        blank=True,
    )
    #
    discoverymethod = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    #
    disc_year = models.IntegerField(
        null=True,
        blank=True,
    )
    #
    disc_facility = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    soltype = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    #
    pl_controv_flag = models.IntegerField(
        null=True,
        blank=True,
    )
    #
    pl_refname = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    #
    pl_orbper = models.FloatField(
        null=True,
        blank=True,
    )
    pl_orbpererr1 = models.FloatField(
        null=True,
        blank=True,
    )
    pl_orbpererr2 = models.FloatField(
        null=True,
        blank=True,
    )
    pl_orbperlim = models.FloatField(
        null=True,
        blank=True,
    )
    pl_orbsmax = models.FloatField(
        null=True,
        blank=True,
    )
    pl_orbsmaxerr1 = models.FloatField(
        null=True,
        blank=True,
    )
    pl_orbsmaxerr2 = models.FloatField(
        null=True,
        blank=True,
    )
    pl_orbsmaxlim = models.FloatField(
        null=True,
        blank=True,
    )
    pl_rade = models.FloatField(
        null=True,
        blank=True,
    )
    pl_radeerr1 = models.FloatField(
        null=True,
        blank=True,
    )
    pl_radeerr2 = models.FloatField(
        null=True,
        blank=True,
    )
    pl_radelim = models.FloatField(
        null=True,
        blank=True,
    )
    pl_radj = models.FloatField(
        null=True,
        blank=True,
    )
    pl_radjerr1 = models.FloatField(
        null=True,
        blank=True,
    )
    pl_radjerr2 = models.FloatField(
        null=True,
        blank=True,
    )
    pl_radjlim = models.FloatField(
        null=True,
        blank=True,
    )
    pl_bmasse = models.FloatField(
        null=True,
        blank=True,
    )
    pl_bmasseerr1 = models.FloatField(
        null=True,
        blank=True,
    )
    pl_bmasseerr2 = models.FloatField(
        null=True,
        blank=True,
    )
    pl_bmasselim = models.FloatField(
        null=True,
        blank=True,
    )
    pl_bmassj = models.FloatField(
        null=True,
        blank=True,
    )
    pl_bmassjerr1 = models.FloatField(
        null=True,
        blank=True,
    )
    pl_bmassjerr2 = models.FloatField(
        null=True,
        blank=True,
    )
    pl_bmassjlim = models.FloatField(
        null=True,
        blank=True,
    )
    #
    pl_bmassprov = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    #
    pl_orbeccen = models.FloatField(
        null=True,
        blank=True,
    )
    pl_orbeccenerr1 = models.FloatField(
        null=True,
        blank=True,
    )
    pl_orbeccenerr2 = models.FloatField(
        null=True,
        blank=True,
    )
    pl_orbeccenlim = models.FloatField(
        null=True,
        blank=True,
    )
    pl_insol = models.FloatField(
        null=True,
        blank=True,
    )
    pl_insolerr1 = models.FloatField(
        null=True,
        blank=True,
    )
    pl_insolerr2 = models.FloatField(
        null=True,
        blank=True,
    )
    pl_insollim = models.FloatField(
        null=True,
        blank=True,
    )
    pl_eqt = models.FloatField(
        null=True,
        blank=True,
    )
    pl_eqterr1 = models.FloatField(
        null=True,
        blank=True,
    )
    pl_eqterr2 = models.FloatField(
        null=True,
        blank=True,
    )
    pl_eqtlim = models.FloatField(
        null=True,
        blank=True,
    )
    #
    ttv_flag = models.IntegerField(
        null=True,
        blank=True,
    )
    #
    st_refname = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    st_spectype = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    #
    st_teff = models.FloatField(
        null=True,
        blank=True,
    )
    st_tefferr1 = models.FloatField(
        null=True,
        blank=True,
    )
    st_tefferr2 = models.FloatField(
        null=True,
        blank=True,
    )
    st_tefflim = models.FloatField(
        null=True,
        blank=True,
    )
    st_rad = models.FloatField(
        max_length=255,
        null=True,
        blank=True,
    )
    st_raderr1 = models.FloatField(
        max_length=255,
        null=True,
        blank=True,
    )
    st_raderr2 = models.FloatField(
        max_length=255,
        null=True,
        blank=True,
    )
    st_radlim = models.FloatField(
        null=True,
        blank=True,
    )
    st_mass = models.FloatField(
        null=True,
        blank=True,
    )
    st_masserr1 = models.FloatField(
        null=True,
        blank=True,
    )
    st_masserr2 = models.FloatField(
        null=True,
        blank=True,
    )
    st_masslim = models.FloatField(
        null=True,
        blank=True,
    )
    st_met = models.FloatField(
        null=True,
        blank=True,
    )
    st_meterr1 = models.FloatField(
        null=True,
        blank=True,
    )
    st_meterr2 = models.FloatField(
        null=True,
        blank=True,
    )
    st_metlim = models.FloatField(
        null=True,
        blank=True,
    )
    #
    st_metratio = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    #
    st_logg = models.FloatField(
        null=True,
        blank=True,
    )
    st_loggerr1 = models.FloatField(
        null=True,
        blank=True,
    )
    st_loggerr2 = models.FloatField(
        null=True,
        blank=True,
    )
    st_logglim = models.FloatField(
        null=True,
        blank=True,
    )
    #
    sy_refname = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    rastr = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    #
    ra = models.FloatField(
        null=True,
        blank=True,
    )
    #
    decstr = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    #
    dec = models.FloatField(
        null=True,
        blank=True,
    )
    #
    sy_dist = models.FloatField(
        null=True,
        blank=True,
    )
    sy_disterr1 = models.FloatField(
        null=True,
        blank=True,
    )
    sy_disterr2 = models.FloatField(
        null=True,
        blank=True,
    )
    sy_vmag = models.FloatField(
        null=True,
        blank=True,
    )
    sy_vmagerr1 = models.FloatField(
        null=True,
        blank=True,
    )
    sy_vmagerr2 = models.FloatField(
        null=True,
        blank=True,
    )
    sy_kmag = models.FloatField(
        null=True,
        blank=True,
    )
    sy_kmagerr1 = models.FloatField(
        null=True,
        blank=True,
    )
    sy_kmagerr2 = models.FloatField(
        null=True,
        blank=True,
    )
    sy_gaiamag = models.FloatField(
        null=True,
        blank=True,
    )
    sy_gaiamagerr1 = models.FloatField(
        null=True,
        blank=True,
    )
    sy_gaiamagerr2 = models.FloatField(
        null=True,
        blank=True,
    )
    #
    rowupdate = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    pl_pubdate = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    releasedate = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.pl_name
