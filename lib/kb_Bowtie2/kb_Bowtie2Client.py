# -*- coding: utf-8 -*-
############################################################
#
# Autogenerated by the KBase type compiler -
# any changes made here will be overwritten
#
############################################################

from __future__ import print_function
# the following is a hack to get the baseclient to import whether we're in a
# package or not. This makes pep8 unhappy hence the annotations.
try:
    # baseclient and this client are in a package
    from .baseclient import BaseClient as _BaseClient  # @UnusedImport
except:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport


class kb_Bowtie2(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://kbase.us/services/authorization/Sessions/Login'):
        if url is None:
            raise ValueError('A url is required')
        self._service_ver = None
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc)

    def align_reads_to_assembly_app(self, params, context=None):
        """
        :param params: instance of type "AlignReadsParams" (Will align the
           input reads (or set of reads specified in a SampleSet) to the
           specified assembly or assembly for the specified Genome (accepts
           Assembly, ContigSet, or Genome types) and produces a
           ReadsAlignment object, or in the case of a SampleSet, a
           ReadsAlignmentSet object. required: input_ref - ref to either a
           SingleEnd/PairedEnd reads, or a SampleSet input (eventually should
           support a ReadsSet as well) assembly_or_genome - ref to Assembly,
           ContigSet, or Genome output_name - name of the output
           ReadsAlignment or ReadsAlignmentSet output_workspace - name or id
           of the WS to save the results to optional: ...) -> structure:
           parameter "input_ref" of String, parameter
           "assembly_or_genome_ref" of String, parameter "output_name" of
           String, parameter "output_workspace" of String, parameter
           "output_alignment_filename_extension" of String, parameter
           "phred33" of String, parameter "phred64" of String, parameter
           "local" of String, parameter "very-fast" of String, parameter
           "fast" of String, parameter "very-sensitive" of String, parameter
           "sensitive" of String, parameter "very-fast-local" of String,
           parameter "very-sensitive-local" of String, parameter "fast-local"
           of String, parameter "fast-sensitive" of String, parameter
           "quality_score" of String, parameter "alignment_type" of String,
           parameter "trim5" of Long, parameter "trim3" of Long, parameter
           "np" of Long, parameter "preset_options" of String, parameter
           "minins" of Long, parameter "maxins" of Long, parameter
           "orientation" of String, parameter "concurrent_njsw_tasks" of
           Long, parameter "concurrent_local_tasks" of Long
        :returns: instance of type "AlignReadsResult" -> structure: parameter
           "reads_alignment_ref" of String, parameter
           "read_alignment_set_ref" of String, parameter "report_name" of
           String, parameter "report_ref" of String
        """
        return self._client.call_method(
            'kb_Bowtie2.align_reads_to_assembly_app',
            [params], self._service_ver, context)

    def align_one_reads_to_assembly(self, context=None):
        """
        aligns a single reads object to produce
        """
        return self._client.call_method(
            'kb_Bowtie2.align_one_reads_to_assembly',
            [], self._service_ver, context)

    def get_bowtie2_index(self, params, context=None):
        """
        :param params: instance of type "GetBowtie2Index" (Provide a
           reference to either an Assembly or Genome to get a Bowtie2 index.
           output_dir is optional, if provided the index files will be saved
           in that directory.  If not, a directory will be generated for you
           and returned by this function.  If specifying the output_dir, the
           directory must not exist yet (to ensure only the index files are
           added there). Currently, Bowtie2 indexes are cached to a WS
           object.  If that object does not exist, then calling this function
           can create a new object.  To create the cache, you must specify
           the ws name or ID in 'ws_for_cache' in which to create the cached
           index.  If this field is not set, the result will not be cached. 
           This parameter will eventually be deprecated once the big file
           cache service is implemented.) -> structure: parameter "ref" of
           String, parameter "output_dir" of String, parameter "ws_for_cache"
           of String
        :returns: instance of type "GetBowtie2IndexResult" (output_dir - the
           folder containing the index files from_cache - 0 if the index was
           built fresh, 1 if it was found in the cache pushed_to_cache - if
           the index was rebuilt and successfully added to the cache, this
           will be set to 1; otherwise set to 0) -> structure: parameter
           "output_dir" of String, parameter "from_cache" of type "boolean"
           (A boolean - 0 for false, 1 for true. @range (0, 1)), parameter
           "pushed_to_cache" of type "boolean" (A boolean - 0 for false, 1
           for true. @range (0, 1))
        """
        return self._client.call_method(
            'kb_Bowtie2.get_bowtie2_index',
            [params], self._service_ver, context)

    def run_bowtie2_cli(self, params, context=None):
        """
        general purpose local function for running tools in the bowtie2 suite
        :param params: instance of type "RunBowtie2CLIParams" (supported
           commands: bowtie2 bowtie2-align-l bowtie2-align-s bowtie2-build
           bowtie2-build-l bowtie2-build-s bowtie2-inspect bowtie2-inspect-l
           bowtie2-inspect-s) -> structure: parameter "command_name" of
           String, parameter "options" of list of String
        """
        return self._client.call_method(
            'kb_Bowtie2.run_bowtie2_cli',
            [params], self._service_ver, context)

    def status(self, context=None):
        return self._client.call_method('kb_Bowtie2.status',
                                        [], self._service_ver, context)
